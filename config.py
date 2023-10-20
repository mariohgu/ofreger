from psycopg2 import connect, extras

host = "localhost"
port = 5432
dbname = "ofreger"
user = "admin"
password = "admin"


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn
