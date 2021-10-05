import logging
from .core import some_function

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info(f'__name__: {__name__}')
    some_function('run1')
    some_function('run2')