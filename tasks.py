import csv
import datetime
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Optional, Iterator

from api_client import YandexWeatherAPI, logger
from schemas import Weathers
from utils import ERR_MESSAGE_TEMPLATE


class CalculatedCity:

    def __init__(self):
        self.calculated_weather: dict[datetime.date, dict[str, int]] = {}
        self._average_good_condition: Optional[int] = None
        self._average_good_temps: Optional[float] = None

    def put(self, date: datetime.date, good_temps: int, good_condition: int) -> None:
        self.calculated_weather[date] = {
            'good_temps': good_temps,
            'good_condition': good_condition
        }
        self._average_good_condition = None
        self._average_good_temps = None

    @property
    def average_good_condition(self) -> int:
        if self._average_good_condition is None:
            self._average_good_condition = int(
                statistics.mean(
                    [
                        x.get('good_condition') for x in self.calculated_weather.values()
                    ]  # type: ignore
                )
            )

        return self._average_good_condition

    @property
    def average_good_temps(self) -> float:
        if self._average_good_temps is None:
            self._average_good_temps = round(
                statistics.mean(
                    [
                        x.get('good_temps') for x in self.calculated_weather.values()
                    ]
                ),  # type: ignore
                1
            )

        return self._average_good_temps

    def __lt__(self, other) -> bool:
        if other.average_good_temps == self.average_good_temps:
            return not other.average_good_condition < self.average_good_condition

        return not other.average_good_temps < self.average_good_temps

    def __eq__(self, other) -> bool:
        return (self.average_good_temps == other.average_good_temps
                ) and (self.average_good_condition == other.average_good_condition)


class DataFetchingTask:
    """
    Получение информацию о погодных условиях для указанного списка городов, используя
    API Яндекс Погоды.
    """

    def __init__(self, cities: list[str]) -> None:
        self.cities = cities

    def get_weather(self) -> Iterator[tuple[str, Weathers]]:
        with ThreadPoolExecutor() as pool:
            return pool.map(self.get_weather_for_city, self.cities)

    @staticmethod
    def get_weather_for_city(city_name) -> tuple[str, Weathers]:
        ywAPI = YandexWeatherAPI()
        return city_name, Weathers.parse_obj(ywAPI.get_forecasting(city_name))


class DataCalculationTask:
    """
    Вычисляем среднюю температуру и проанализируйте информацию об осадках
    за указанный период для всех городов.
    """

    def __init__(self) -> None:
        self.good_condition: list[str] = []
        self.good_temps: list[int] = []
        self.calculated_weather = CalculatedCity()

    def run(self, raw_weathers: tuple[str, Weathers]) -> tuple[str, CalculatedCity]:
        city, weathers = raw_weathers
        for weather_on_date in weathers.forecasts:
            self.good_condition = []
            self.good_temps = []
            for hour in weather_on_date.hours:
                if 9 <= int(hour.hour) <= 19:
                    self.good_temps.append(int(hour.temp))

                    if hour.condition in ['clear', 'partly-cloudy', 'cloudy', 'overcast']:
                        self.good_condition.append(hour.condition)

            if self.good_temps:
                self.calculated_weather.put(
                    date=datetime.datetime.strptime(weather_on_date.date, "%Y-%m-%d").date(),
                    good_temps=int(statistics.mean(self.good_temps)),
                    good_condition=len(self.good_condition)
                )

        return city, self.calculated_weather


class DataAggregationTask:
    def create_csv_file(self, data: list[list[Any]], headers: list[str]) -> str:

        csv_filename = 'output.csv'

        with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
            try:
                writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
                if headers is not None:
                    f.writelines('sep=,' + '\n')
                    writer.writerow(headers)
                for element in data:
                    writer.writerow(element)

                logger.info(f'Create file {csv_filename}')

                return csv_filename

            except Exception as ex:
                logger.error(ex)
                raise Exception(ERR_MESSAGE_TEMPLATE)

    def run(
            self,
            calculation_weather_statistics: list[tuple[str, CalculatedCity]]
    ) -> list[tuple[str, CalculatedCity]]:
        sort_calculation_weather_statistics = sorted(
            calculation_weather_statistics,
            reverse=True,
            key=lambda x: x[1]
        )

        unique_date = set()

        for count, calculation_weather_statistic in enumerate(sort_calculation_weather_statistics):
            for date in calculation_weather_statistic[1].calculated_weather.keys():
                unique_date.add(date)

            list_unique_date = sorted(list(unique_date))

        headers = [
            'Город/день', '', *[
                f'{date.day:02}-{date.month:02}' for date in list_unique_date
            ], 'Среднее', 'Рейтинг'
        ]

        data = []

        for count, calculation_weather_statistic in enumerate(sort_calculation_weather_statistics):
            city, weather = calculation_weather_statistic
            row1: list[Any] = [city, 'Температура, среднее']
            row2: list[Any] = ['', 'Без осадков, часов']

            for date in list_unique_date:
                if weather_om_date := weather.calculated_weather.get(date):
                    row1.append(weather_om_date.get('good_temps'))
                    row2.append(weather_om_date.get('good_condition'))
                else:
                    row1.append(None)
                    row2.append(None)
            row1.append(weather.average_good_temps)
            row1.append(count + 1)
            row2.append(weather.average_good_condition)

            data.append(row1)
            data.append(row2)

        self.create_csv_file(data=data, headers=headers)

        return sort_calculation_weather_statistics


class DataAnalyzingTask:

    def run(self, sort_calculation_weather_statistics: list[tuple[str, CalculatedCity]]) -> None:
        best_city, best_weather = sort_calculation_weather_statistics[0]
        print('Наиболее благоприятный(е)')
        print(best_city)

        for city, weather in sort_calculation_weather_statistics[1:]:
            if weather == best_weather:
                print(city)
