import logging
import sys
from pytest_logging.core import some_function

logger = logging.getLogger(__name__)

def test():
    logger.info(f'__name__: {__name__}')
    # note that somehow pytest is able to locate the acutal package with some sys.path magic:
    logger.info(f'sys.path: {sys.path}')
    some_function('run1')
    some_function('run2')
