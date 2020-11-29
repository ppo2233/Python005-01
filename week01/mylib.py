import logging


logger = logging.getLogger(__name__)


def do_something():
    logger.info('doing something ....')
    try:
        0 / 0
    except Exception as e:
        logger.error(f'got error: {e}')
