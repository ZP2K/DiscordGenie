import psycopg2

import config.build_config as config


def get_tasks():
    dbname = config.read_dbname()
    dbuser = config.read_dbuser()
    dbpass = config.read_dbpass()
    try:
        connect_str = "dbname='{}' user='{}' host='localhost' password={}".format(dbname, dbuser, dbpass)
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        cursor.execute("""SELECT * from tasks""")
        tasks = cursor.fetchall()
        return tasks
    except:
        print("failed to get db")
