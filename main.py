from traceback import format_exc
from dotenv import load_dotenv

load_dotenv()

from src.files import create_multiple_file
from src.constants import ERROR_LOG_PATH, LOG_PATH, DEV_MODE
from src.logger import Logger
from logging import DEBUG, ERROR

import sys

# from logger.py
create_multiple_file(ERROR_LOG_PATH, LOG_PATH)
error_log = Logger.setup_logger("error", ERROR_LOG_PATH, ERROR)
log = Logger.setup_logger(file_path=LOG_PATH, level=DEBUG)

def main():
    pass
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        log.info("uscita in corso...\n----------------------------")
    except Exception as e: 
        if DEV_MODE == False:                    # catch *all* exceptions
            error_log.critical("Unexpected error: " + str(sys.exc_info()[0]) + " : " + str(sys.exc_info()[1]))
        else:
            print(format_exc())
