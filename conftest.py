import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import pytest
import json
from database.db_connection import connect_db
from utils.config_reader import get_config


@pytest.fixture(scope="session")
def config():
    return get_config()


@pytest.fixture(scope="session")
def base_url(config):
    return config["API"]["base_url"]


@pytest.fixture(scope="session")
def db_connection():
    connection = connect_db()
    yield connection
    connection.close()


@pytest.fixture
def test_data():
    with open("test_data/user_data.json") as file:
        return json.load(file)
