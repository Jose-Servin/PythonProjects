import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='joseservin',
        user='postgres',
        password='Baker'
    )
    return conn
