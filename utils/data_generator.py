import random
import string
import time
import os
from utils.log import log
from datetime import datetime
from configparser import ConfigParser


def get_random_string(length: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def get_unique_integer() -> int:
    return int(time.time())


def get_current_date_and_time():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H:%M:%S")
    return formatted_date


def getConfig(ckey, cvalue, BASE_DIR=None):
    config = ConfigParser()
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config.ini"
    )
    config.read(config_path)
    log.info(f"{ckey}-{ckey}-{BASE_DIR}")
    if BASE_DIR:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        test_case_data = config.get(ckey, cvalue)
        return os.path.join(BASE_DIR, test_case_data)
    return config.get(ckey, cvalue)
