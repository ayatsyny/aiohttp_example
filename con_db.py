from mysql import connector
from mysql.connector import Error
from settings import MYSQL_HOST, MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_USER


def with_connection(func):
    def wrapper(*args, **kwargs):
        try:
            conn = connector.connect(host=MYSQL_HOST, database=MYSQL_DATABASE, user=MYSQL_USER, password=MYSQL_PASSWORD)
            if not conn.is_connected():
                raise ConnectionAbortedError('Not connected to MySQL database')
            result = func(conn, *args, **kwargs)
        except Error as e:
            print(e)
            return
        finally:
            conn.close()
        return result
    return wrapper


@with_connection
def save_db(conn, query, *args):
    cur = conn.cursor()
    cur.execute(query, args)
    if not cur.lastrowid:
        print('last insert id not found')
    conn.commit()


@with_connection
def get_all_rows(conn, query):
    cur = conn.cursor()
    cur.execute(query)

    res = []
    for row in cur.fetchall():
        res.append(row)
    return res
