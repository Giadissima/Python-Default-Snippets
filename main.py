from src.costants import ERROR_LOG_PATH, LOG_PATH
from src.logger import Logger
from logging import DEBUG, ERROR
import sys

# from logger.py
error_log = Logger.setup_logger("error", ERROR_LOG_PATH, ERROR)
log = Logger.setup_logger(file_path=LOG_PATH, level=DEBUG)

def main():
    pass
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        log.info("uscita in corso...\n----------------------------")
    except Exception as e:                    # catch *all* exceptions
        error_log.critical("Unexpected error: " + str(sys.exc_info()[0]) + " : " + str(sys.exc_info()[1]))
