from src.Logging import logger_test_insert_to_bd, current_function_name
import pymysql


class MySQL:

    def __init__(self, host, port, user, password, db_name):
        connect_str = f"{host} {port} {user} {password} {db_name}"
        logger_test_insert_to_bd.log_info(connect_str)
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

    def select_all_data_from_table(self, table_name):

        select_all_rows = f"SELECT * FROM {table_name};"
        with self.connection.cursor() as cursor:
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            return rows

    def select_order_id_and_order_code_from_orders(self, order_id, order_code):
        insert_query = (f"SELECT * FROM orders "
                        f"WHERE order_id={order_id} AND order_code={order_code};")
        logger_test_insert_to_bd.log_info(
            f'\n Function name: {current_function_name()}. '
            '\n Query: ' + insert_query + "\n")
        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            rows = cursor.fetchall()
            return rows

    def add_to_order(self, order_id, service_fields, protocol, order_code):
        insert_query = (f"INSERT INTO `orders` (order_id, service_fields, protocol, order_code, dt_add) "
                        f"VALUES ('{order_id}', '{service_fields}', '{protocol}', '{order_code}', NOW());")
        logger_test_insert_to_bd.log_info(f'\n Function name: {current_function_name()} \n Query: '
                                          + insert_query + "\n")

        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def __del__(self, connection):
        connection.close()
