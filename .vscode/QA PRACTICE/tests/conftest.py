from playwright.sync_api import Page, expect
import re
from time import sleep
import pytest
import logging
import os
import datetime

# Настройка логирования
@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    # Создаем папку для логов если её нет
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # Формируем имя файла с текущей датой и временем
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs/test_run_{timestamp}.log"
    
    # Настраиваем логирование
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Вывод в консоль
        ]
    )
    
    return logging.getLogger()

# Делаем логгер доступным в тестах
@pytest.fixture
def logger():
    return logging.getLogger()