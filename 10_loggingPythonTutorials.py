#!/usr/bin/env python3

# https://docs.python.org/3/library/logging.config.html

# thanks to @patloeber's youtube channel

# allow logging to happen
import logging
import logging.config
import traceback
import time

# Get the absolute path in place
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), "logger.conf")
print(log_file_path)
logging.config.fileConfig(log_file_path)

# use the simple example logger from logging.conf
logger = logging.getLogger("simpleExample")
logger.debug("Test debug with simpl example logger")

# useful to add the name of the module
# logger = logging.getLogger(__name__)


# needs to be setup upfront if you want the debugs turned on
# once logging starts, config cannot be changed
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
# 	                datefmt='%m/%d/%y %H:%M:%S')

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

# avoid propagation to the upper levels. or base logger
logger.propagate = False


try:
    a = [1, 2, 3]
    # a[4] = 0 # to force an exception
except IndexError as e:
    logger.error("The error is %s", traceback.format_exc())
    # logger.error(e, exc_infp=True)

# Instead of the below methods of handlers
# please create a logger.conf - see the that file

# rotating log files
# from logging.handlers import RotatingFileHandler

# if you want to use a time based rollover
from logging.handlers import TimedRotatingFileHandler

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
handler = TimedRotatingFileHandler("timed_app.log", when="s", interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(100):
    logger.error("error file rotation")
    time.sleep(5)

# create handlers that logs to a stream
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# set levels and formats
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# setup formatters if the basic config above is not used
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is a warning")
logger.error("this is an error")
logger.info("this is info")
