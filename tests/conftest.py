import datetime

import pytest

from schemas import DetailWeatherSchema, GeneralWeatherSchema, WeathersSchema
from tasks import CalculatedCity


@pytest.fixture()
def calculated_city():
    calculated_city = CalculatedCity()
    calculated_city.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    calculated_city.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    return calculated_city


@pytest.fixture()
def raw_weathers():
    return (
        'CAIRO',
        WeathersSchema(
            forecasts=[
                GeneralWeatherSchema(
                    date='2022-05-26',
                    hours=[
                        DetailWeatherSchema(hour='0', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='1', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='2', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='3', temp=21, condition='clear'),
                        DetailWeatherSchema(hour='4', temp=20, condition='clear'),
                        DetailWeatherSchema(hour='5', temp=19, condition='clear'),
                        DetailWeatherSchema(hour='6', temp=20, condition='clear'),
                        DetailWeatherSchema(hour='7', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='8', temp=24, condition='clear'),
                        DetailWeatherSchema(hour='9', temp=27, condition='clear'),
                        DetailWeatherSchema(hour='10', temp=30, condition='clear'),
                        DetailWeatherSchema(hour='11', temp=31, condition='clear'),
                        DetailWeatherSchema(hour='12', temp=32, condition='clear'),
                        DetailWeatherSchema(hour='13', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='14', temp=35, condition='clear'),
                        DetailWeatherSchema(hour='15', temp=35, condition='clear'),
                        DetailWeatherSchema(hour='16', temp=35, condition='clear'),
                        DetailWeatherSchema(hour='17', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='18', temp=33, condition='clear'),
                        DetailWeatherSchema(hour='19', temp=32, condition='clear'),
                        DetailWeatherSchema(hour='20', temp=30, condition='clear'),
                        DetailWeatherSchema(hour='21', temp=29, condition='clear'),
                        DetailWeatherSchema(hour='22', temp=27, condition='clear'),
                        DetailWeatherSchema(hour='23', temp=26, condition='clear')
                    ]
                ),
                GeneralWeatherSchema(
                    date='2022-05-27',
                    hours=[
                        DetailWeatherSchema(hour='0', temp=25, condition='clear'),
                        DetailWeatherSchema(hour='1', temp=24, condition='clear'),
                        DetailWeatherSchema(hour='2', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='3', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='4', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='5', temp=21, condition='clear'),
                        DetailWeatherSchema(hour='6', temp=21, condition='clear'),
                        DetailWeatherSchema(hour='7', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='8', temp=25, condition='clear'),
                        DetailWeatherSchema(hour='9', temp=28, condition='clear'),
                        DetailWeatherSchema(hour='10', temp=29, condition='clear'),
                        DetailWeatherSchema(hour='11', temp=31, condition='clear'),
                        DetailWeatherSchema(hour='12', temp=33, condition='clear'),
                        DetailWeatherSchema(hour='13', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='14', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='15', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='16', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='17', temp=35, condition='clear'),
                        DetailWeatherSchema(hour='18', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='19', temp=33, condition='clear'),
                        DetailWeatherSchema(hour='20', temp=31, condition='clear'),
                        DetailWeatherSchema(hour='21', temp=30, condition='clear'),
                        DetailWeatherSchema(hour='22', temp=28, condition='clear'),
                        DetailWeatherSchema(hour='23', temp=27, condition='clear')
                    ]
                ),
                GeneralWeatherSchema(
                    date='2022-05-28',
                    hours=[
                        DetailWeatherSchema(hour='0', temp=26, condition='clear'),
                        DetailWeatherSchema(hour='1', temp=25, condition='clear'),
                        DetailWeatherSchema(hour='2', temp=24, condition='clear'),
                        DetailWeatherSchema(hour='3', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='4', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='5', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='6', temp=22, condition='clear'),
                        DetailWeatherSchema(hour='7', temp=24, condition='clear'),
                        DetailWeatherSchema(hour='8', temp=26, condition='clear'),
                        DetailWeatherSchema(hour='9', temp=28, condition='clear'),
                        DetailWeatherSchema(hour='10', temp=31, condition='clear'),
                        DetailWeatherSchema(hour='11', temp=33, condition='clear'),
                        DetailWeatherSchema(hour='12', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='13', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='14', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='15', temp=37, condition='clear'),
                        DetailWeatherSchema(hour='16', temp=37, condition='clear'),
                        DetailWeatherSchema(hour='17', temp=37, condition='clear'),
                        DetailWeatherSchema(hour='18', temp=36, condition='clear'),
                        DetailWeatherSchema(hour='19', temp=34, condition='clear'),
                        DetailWeatherSchema(hour='20', temp=33, condition='clear'),
                        DetailWeatherSchema(hour='21', temp=31, condition='clear'),
                        DetailWeatherSchema(hour='22', temp=29, condition='clear'),
                        DetailWeatherSchema(hour='23', temp=28, condition='clear')
                    ]
                ),
                GeneralWeatherSchema(
                    date='2022-05-29',
                    hours=[
                        DetailWeatherSchema(hour='0', temp=27, condition='clear'),
                        DetailWeatherSchema(hour='1', temp=26, condition='clear'),
                        DetailWeatherSchema(hour='2', temp=25, condition='clear'),
                        DetailWeatherSchema(hour='3', temp=24, condition='clear'),
                        DetailWeatherSchema(hour='4', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='5', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='6', temp=23, condition='clear'),
                        DetailWeatherSchema(hour='7', temp=26, condition='clear'),
                        DetailWeatherSchema(hour='8', temp=28, condition='clear')
                    ]
                ),
                GeneralWeatherSchema(
                    date='2022-05-30',
                    hours=[]
                )
            ]
        )
    )


@pytest.fixture()
def calculation_weather_statistics():
    calculated_city1 = CalculatedCity()
    calculated_city1.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    calculated_city1.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    calculated_city2 = CalculatedCity()
    calculated_city2.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    calculated_city2.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    return [
        ('MOSCOW', calculated_city1),
        ('PARIS', calculated_city2),
    ]


@pytest.fixture()
def sort_calculation_weather_statistics():
    calculated_city1 = CalculatedCity()
    calculated_city1.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    calculated_city1.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    calculated_city2 = CalculatedCity()
    calculated_city2.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    calculated_city2.put(datetime.date(year=2022, month=1, day=1), 9, 9)
    return [
        ('PARIS', calculated_city2),
        ('MOSCOW', calculated_city1),
    ]


@pytest.fixture()
def control_csv_file():
    return '''sep=,
"Город/день","","01-01","02-01","Среднее","Рейтинг"
"PARIS","Температура, среднее","9","","9","1"
"","Без осадков, часов","9","","9"
"MOSCOW","Температура, среднее","6","9","7.5","2"
"","Без осадков, часов","6","9","7"
'''
