import pymysql

from test_framework.src.helpers.config_helpers import get_database_credentials
from test_framework.src.configs.generic_configs import GenericConfigs


def read_from_db(sql):
    db_creds = get_database_credentials()
    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'], user=db_creds['db_user'], password=db_creds['db_password'])
    try:
        cursor_item = connection.cursor(pymysql.cursors.DictCursor)
        cursor_item.execute(sql)
        db_data = cursor_item.fetchall()
        cursor_item.close()
    finally:
        connection.close()
    return db_data


def get_order_from_db_by_order_no(order_no):
    schema = GenericConfigs.DATABASE_SCHEMA
    table = GenericConfigs.DATABASE_TABLE_ORDERS
    sql = f"SELECT * FROM {schema}.{table} WHERE ID={order_no} AND post_type='shop_order';"

    db_order = read_from_db(sql)
    return db_order


#print(get_order_from_db_by_order_no(70))
