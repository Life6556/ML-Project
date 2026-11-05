import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s-%(lineno)d-%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)

# def divide(x,y):
#     try:
#         result=x/y
#         logging.info(f"division successfull..result:{result}")
#     except Exception as e:
#         logging.exception(f"erorr:{e}")
# divide(10,12)
# divide(5,0)
# logging.basicConfig(
#     filename="app.log",
#     level=logging.DEBUG,
#     format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d",
#     filemode="a",
#     datefmt="%d-%m-%Y %H:%M:%S",
#     encoding="utf-8"

# )

# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")
# logging.info("আমি Python Logging শিখছ")