import inspect
import logging
import logging.config


def getlogger():
    logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)
    calling_function = inspect.stack()[1][3]
    logger = logging.getLogger(calling_function)
    return logger

