import logging

module_logger = logging.getLogger(__name__)


def some_function(id: str):
    print()
    print(f'__name__: {__name__}: {id} ')
    print(f'stdout logging: {id}')
    logger = module_logger.getChild(id)
    logger.debug(f'debug logging: {id}')
    logger.info(f'info logging: {id}')
    logger.warning(f'warning logging: {id}')
    logger.error(f'error logging: {id}')
    pass