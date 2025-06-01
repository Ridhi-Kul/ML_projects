# Logger is to log information, execution of a file in case there is some error (custom exception) in a text file
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # The file name that will be created will have whatever date time is there
logs_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(logs_path, exist_ok = True) # Even though there is a folder keep on appending the files inside that

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

'''
line 6: Create timestamped log file name
line 7: Path to logs folder
line 8: If the path does not exists then create, otherwise okay
line 9: FUll path to log file inside the logs folder
'''
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, 
)

# Whenever we get an exception, we will log it with a logger file and use logging.info to put it inside the file