#!/usr/bin/env python3

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


# Create a logger
logger = logging.getLogger("DailyLogger")
logger.setLevel(logging.DEBUG)  # Set the desired logging level

# Define a log file name format
log_filename = datetime.now().strftime("log_%d_%m_%Y.log")
log_filename = "logs/" + log_filename

# Create a TimedRotatingFileHandler for daily log rotation
handler = TimedRotatingFileHandler(
    log_filename,
    when="midnight",  # Rotate at midnight
    interval=1,  # Interval of 1 day
    backupCount=7,  # Keep the last 7 log files (optional)
)
handler.suffix = "%d_%m_%Y"  # Set the suffix for the rotated log files
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add the handler to the logger
logger.addHandler(handler)

# Example usage
# logger.info("This is an info message.")
# logger.error("This is an error message.")
