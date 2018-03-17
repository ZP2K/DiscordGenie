import psycopg2

import config.build_config as config


def get_cursor():
    dbname = config.read_dbname()
    dbuser = config.read_dbuser()
    dbpass = config.read_dbpass()
    connect_str = "dbname='{}' user='{}' host='localhost' password={}".format(dbname, dbuser, dbpass)
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    return cursor


def get_tasks():
    cursor = get_cursor()
    cursor.execute("""SELECT * from tasks""")
    tasks = cursor.fetchall()
    return tasks


def set_tasks(request):
    cursor = get_cursor()
    query = "INSERT INTO tasks VALUES (%s, %s);"
    data = ("crypto", request)
    try:
        cursor.execute(query, data)
    except Exception as e:
        print(e)
