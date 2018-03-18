import psycopg2

import config.build_config as config


def get_cursor():
    dbname = config.read_dbname()
    dbuser = config.read_dbuser()
    dbpass = config.read_dbpass()
    connect_str = "dbname='{}' user='{}' host='localhost' password={}".format(dbname, dbuser, dbpass)
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    return cursor, conn


def get_tasks():
    cursor, connect = get_cursor()
    cursor.execute("""SELECT * from tasks""")
    tasks = cursor.fetchall()
    connect.commit()
    return tasks


def set_tasks(request):
    cursor, connect = get_cursor()
    query = "INSERT INTO tasks VALUES (%s, %s);"
    data = ("crypto", request)
    cursor.execute(query, data)
    connect.commit()


def set_star():
    cursor, connect = get_cursor()
    query = "UPDATE MEMESTARS SET count = count + 1 WHERE NAME='bot';"
    cursor.execute(query)
    connect.commit()


def get_stars():
    cursor, connect = get_cursor()
    query = "SELECT count from MEMESTARS where name = 'bot'"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    connect.commit()
    return count
