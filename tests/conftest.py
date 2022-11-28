import datetime

import pytest

from schemas import Weathers, GeneralWeather, DetailWeather
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
        Weathers(
            forecasts=[
                GeneralWeather(
                    date='2022-05-26',
                    hours=[
                        DetailWeather(hour='0', temp=23, condition='clear'),
                        DetailWeather(hour='1', temp=23, condition='clear'),
                        DetailWeather(hour='2', temp=22, condition='clear'),
                        DetailWeather(hour='3', temp=21, condition='clear'),
                        DetailWeather(hour='4', temp=20, condition='clear'),
                        DetailWeather(hour='5', temp=19, condition='clear'),
                        DetailWeather(hour='6', temp=20, condition='clear'),
                        DetailWeather(hour='7', temp=22, condition='clear'),
                        DetailWeather(hour='8', temp=24, condition='clear'),
                        DetailWeather(hour='9', temp=27, condition='clear'),
                        DetailWeather(hour='10', temp=30, condition='clear'),
                        DetailWeather(hour='11', temp=31, condition='clear'),
                        DetailWeather(hour='12', temp=32, condition='clear'),
                        DetailWeather(hour='13', temp=34, condition='clear'),
                        DetailWeather(hour='14', temp=35, condition='clear'),
                        DetailWeather(hour='15', temp=35, condition='clear'),
                        DetailWeather(hour='16', temp=35, condition='clear'),
                        DetailWeather(hour='17', temp=34, condition='clear'),
                        DetailWeather(hour='18', temp=33, condition='clear'),
                        DetailWeather(hour='19', temp=32, condition='clear'),
                        DetailWeather(hour='20', temp=30, condition='clear'),
                        DetailWeather(hour='21', temp=29, condition='clear'),
                        DetailWeather(hour='22', temp=27, condition='clear'),
                        DetailWeather(hour='23', temp=26, condition='clear')
                    ]
                ),
                GeneralWeather(
                    date='2022-05-27',
                    hours=[
                        DetailWeather(hour='0', temp=25, condition='clear'),
                        DetailWeather(hour='1', temp=24, condition='clear'),
                        DetailWeather(hour='2', temp=23, condition='clear'),
                        DetailWeather(hour='3', temp=22, condition='clear'),
                        DetailWeather(hour='4', temp=22, condition='clear'),
                        DetailWeather(hour='5', temp=21, condition='clear'),
                        DetailWeather(hour='6', temp=21, condition='clear'),
                        DetailWeather(hour='7', temp=23, condition='clear'),
                        DetailWeather(hour='8', temp=25, condition='clear'),
                        DetailWeather(hour='9', temp=28, condition='clear'),
                        DetailWeather(hour='10', temp=29, condition='clear'),
                        DetailWeather(hour='11', temp=31, condition='clear'),
                        DetailWeather(hour='12', temp=33, condition='clear'),
                        DetailWeather(hour='13', temp=34, condition='clear'),
                        DetailWeather(hour='14', temp=36, condition='clear'),
                        DetailWeather(hour='15', temp=36, condition='clear'),
                        DetailWeather(hour='16', temp=36, condition='clear'),
                        DetailWeather(hour='17', temp=35, condition='clear'),
                        DetailWeather(hour='18', temp=34, condition='clear'),
                        DetailWeather(hour='19', temp=33, condition='clear'),
                        DetailWeather(hour='20', temp=31, condition='clear'),
                        DetailWeather(hour='21', temp=30, condition='clear'),
                        DetailWeather(hour='22', temp=28, condition='clear'),
                        DetailWeather(hour='23', temp=27, condition='clear')
                    ]
                ),
                GeneralWeather(
                    date='2022-05-28',
                    hours=[
                        DetailWeather(hour='0', temp=26, condition='clear'),
                        DetailWeather(hour='1', temp=25, condition='clear'),
                        DetailWeather(hour='2', temp=24, condition='clear'),
                        DetailWeather(hour='3', temp=23, condition='clear'),
                        DetailWeather(hour='4', temp=23, condition='clear'),
                        DetailWeather(hour='5', temp=22, condition='clear'),
                        DetailWeather(hour='6', temp=22, condition='clear'),
                        DetailWeather(hour='7', temp=24, condition='clear'),
                        DetailWeather(hour='8', temp=26, condition='clear'),
                        DetailWeather(hour='9', temp=28, condition='clear'),
                        DetailWeather(hour='10', temp=31, condition='clear'),
                        DetailWeather(hour='11', temp=33, condition='clear'),
                        DetailWeather(hour='12', temp=34, condition='clear'),
                        DetailWeather(hour='13', temp=36, condition='clear'),
                        DetailWeather(hour='14', temp=36, condition='clear'),
                        DetailWeather(hour='15', temp=37, condition='clear'),
                        DetailWeather(hour='16', temp=37, condition='clear'),
                        DetailWeather(hour='17', temp=37, condition='clear'),
                        DetailWeather(hour='18', temp=36, condition='clear'),
                        DetailWeather(hour='19', temp=34, condition='clear'),
                        DetailWeather(hour='20', temp=33, condition='clear'),
                        DetailWeather(hour='21', temp=31, condition='clear'),
                        DetailWeather(hour='22', temp=29, condition='clear'),
                        DetailWeather(hour='23', temp=28, condition='clear')
                    ]
                ),
                GeneralWeather(
                    date='2022-05-29',
                    hours=[DetailWeather(hour='0', temp=27, condition='clear'),
                           DetailWeather(hour='1', temp=26, condition='clear'),
                           DetailWeather(hour='2', temp=25, condition='clear'),
                           DetailWeather(hour='3', temp=24, condition='clear'),
                           DetailWeather(hour='4', temp=23, condition='clear'),
                           DetailWeather(hour='5', temp=23, condition='clear'),
                           DetailWeather(hour='6', temp=23, condition='clear'),
                           DetailWeather(hour='7', temp=26, condition='clear'),
                           DetailWeather(hour='8', temp=28, condition='clear')
                           ]
                ),
                GeneralWeather(
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
def control_csv_file():
    lines = (
        'sep=,\n',
        '"Город/день","","01-01","02-01","Среднее","Рейтинг"\n',
        '"PARIS","Температура, среднее","6","9","7.5","1"\n',
        '"","Без осадков, часов","6","9","7"\n',
        '"MOSCOW","Температура, среднее","6","9","7.5","2"\n',
        '"","Без осадков, часов","6","9","7"\n'
    )
    return '''sep=,
"Город/день","","01-01","02-01","Среднее","Рейтинг"
"PARIS","Температура, среднее","6","9","7.5","1"
"","Без осадков, часов","6","9","7"
"MOSCOW","Температура, среднее","6","9","7.5","2"
"","Без осадков, часов","6","9","7"
'''
