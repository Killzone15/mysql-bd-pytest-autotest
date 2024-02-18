import random
from src.Logging import logger_test_insert_to_bd
import time
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')


class TestBD:

    def test_insert_add_orders(self, protocol, emulator_store_connection):

        try:
            self.bd = emulator_store_connection
            order_id = random.randint(10000, 99999)
            order_code = random.randint(10000, 99999)
            service_fields = config.get('CONSTANT', "TEST_STRING")
            self.bd.add_to_order(order_id, service_fields, protocol, order_code)

            time.sleep(10)

            data = self.bd.select_order_id_and_order_code_from_orders(order_id, order_code)
            logger_test_insert_to_bd.log_info("\n" + str(data) + "\n")

            service_fields_in_database = data[0]['service_fields']
            protocol_in_database = data[0]['protocol']

            assert service_fields_in_database == service_fields, 'service_fields не равен TEST_STRING'
            assert protocol_in_database == protocol, 'protocol не равен консольному аргументу --procotol'

        except Exception as e:
            error_string = f"Произошло исключение: {str(e)}"
            logger_test_insert_to_bd.log_exception(error_string)
            raise ValueError(error_string)
