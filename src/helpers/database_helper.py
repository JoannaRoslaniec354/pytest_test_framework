import pymysql


def read_from_db(sql):
    connection = pymysql.connect(host='127.0.0.1', port=8889, user='root', password='root')
    try:
        cursor_item = connection.cursor(pymysql.cursors.DictCursor)
        cursor_item.execute(sql)
        db_data = cursor_item.fetchall()
        cursor_item.close()
    finally:
        connection.close()
    return db_data


def get_order_from_db_by_order_no(order_no):
    sql = f"SELECT * FROM quicksitedb.wp_posts WHERE ID={order_no} AND post_type='shop_order';"

    db_order = read_from_db(sql)
    return db_order


#print(get_order_from_db_by_order_no(70))
