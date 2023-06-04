import logger
from logger import logger_info, log_file_r

def log_format(flightmode, altitude, latitude, longitude):
    return '{},{},{},{}'.format(flightmode, altitude, latitude, longitude)

logger_info.info("Hello World")
logger_info.info(log_format('Hold',100,35,135))
print(log_file_r)