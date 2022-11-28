import multiprocessing

from api_client import logger
from tasks import DataAggregationTask, DataAnalyzingTask, DataCalculationTask, DataFetchingTask
from utils import CITIES


def forecast_weather():
    """
    Анализ погодных условий по городам
    """
    logger.info('Script start')

    logger.info('Get metric from server')
    data_fetching_task = DataFetchingTask(CITIES.keys())
    raw_weathers = data_fetching_task.get_weather()
    logger.info('Fetching metric OK.')

    cores_count = multiprocessing.cpu_count()
    logger.info(f'Server {cores_count=}.')

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
    data_analyzing_task.run(sort_calculation_weather_statistics)
    logger.info('Script start')


if __name__ == "__main__":
    forecast_weather()
