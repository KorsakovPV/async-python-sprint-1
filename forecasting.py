import multiprocessing

from api_client import YandexWeatherAPI, logger
from schemas import WeathersSchema
from tasks import DataAggregationTask, DataAnalyzingTask, DataCalculationTask, DataFetchingTask
from utils import CITIES


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    logger.info('Script start')

    cores_count = multiprocessing.cpu_count()
    logger.info(f'Server {cores_count=}.')

    # We use cpu_count + 4 for both types of tasks.
    # But we limit it to 32 to avoid consuming surprisingly large resource
    # on many core machine.
    max_workers = min(32, (cores_count or 1) + 4)

    logger.info(f'Get metric from server in thread with {max_workers=}')
    data_fetching_task = DataFetchingTask(
        cities=CITIES.keys(),
        weather_api=YandexWeatherAPI(),
        weather_schema=WeathersSchema
    )
    raw_weathers = data_fetching_task.get_weather(max_workers=max_workers)
    logger.info('Fetching metric OK.')

    use_cores = cores_count - 1
    logger.info(f'Start calculation {use_cores=}')
    pool = multiprocessing.Pool(processes=use_cores)
    data_calculation_task = DataCalculationTask()
    calculation_weathers = pool.map(data_calculation_task.run, raw_weathers)

    logger.info('Start aggregation.')
    data_aggregation_task = DataAggregationTask()
    sort_calculation_weather_statistics = data_aggregation_task.run(calculation_weathers)

    logger.info('Start analyzing.')
    data_analyzing_task = DataAnalyzingTask()
    list_of_best_city = data_analyzing_task.run(sort_calculation_weather_statistics)

    print('Наиболее благоприятный(е)')
    for city in list_of_best_city:
        print(city)

    logger.info('Script stop')


if __name__ == "__main__":
    forecast_weather()
