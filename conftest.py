import pytest

import configparser
from src.BD import MySQL
from src.Logging import logger_test_insert_to_bd

config = configparser.ConfigParser()
config.read('config/config.ini')


@pytest.fixture(scope="class")
def emulator_store_connection():
    host = config.get('DATABASE.emulator_green', "HOST")
    port = int(config.get('DATABASE.emulator_green', "PORT"))
    user = config.get('DATABASE.emulator_green', "USER")
    password = config.get('DATABASE.emulator_green', "PASSWORD")
    database = config.get('DATABASE.emulator_green', "DB_NAME")

    bd = MySQL(host, port, user, password, database)

    yield bd



def pytest_addoption(parser):
    parser.addoption(
        "--protocol",
        action="store",
        type=int,
        default=0,
        help="Protocol число int"
    )


@pytest.fixture(scope="session")
def protocol(request):
    protocol = request.config.getoption('--protocol')
    if protocol == 0:
        error_string = "Необходимо указать аргумент --protocol"
        logger_test_insert_to_bd.log_error(error_string)
        raise ValueError(error_string)
    return protocol
