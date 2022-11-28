import datetime

from tasks import CalculatedCity, DataCalculationTask, DataAggregationTask


class TestCalculatedCity:

    def test_put(self):
        calculated_city = CalculatedCity()
        calculated_city.put(datetime.date(year=2022, month=1, day=1), 6, 6)
        assert calculated_city.calculated_weather == {datetime.date(year=2022, month=1, day=1): {'good_temps': 6, 'good_condition': 6}}

    def test_average_good_condition(self, calculated_city):
        assert calculated_city.average_good_condition == 7

    def test_average_good_temps(self, calculated_city):
        assert calculated_city.average_good_temps == 7.5


class TestDataCalculationTask:

    def test_run(self, raw_weathers):
        data_calculation_task = DataCalculationTask()
        city, calculated_weather = data_calculation_task.run(raw_weathers)
        assert city == raw_weathers[0]
        assert calculated_weather.average_good_condition == 11
        assert calculated_weather.average_good_temps == 33
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=26)).get('good_temps') == 32
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=26)).get('good_condition') == 11
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=27)).get('good_temps') == 33
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=27)).get('good_condition') == 11
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=28)).get('good_temps') == 34
        assert calculated_weather.calculated_weather.get(datetime.date(year=2022, month=5, day=28)).get('good_condition') == 11


class TestDataAggregationTask:

    def test_run(self, calculation_weather_statistics, control_csv_file, line=None):
        data_aggregation_task = DataAggregationTask()
        sort_calculation_weather_statistics = data_aggregation_task.run(calculation_weather_statistics)
        assert sort_calculation_weather_statistics[0][0] == 'PARIS'
        assert sort_calculation_weather_statistics[1][0] == 'MOSCOW'

        with open('output.csv', 'r', encoding='utf-8') as csv_file:
            assert control_csv_file == csv_file.read()
