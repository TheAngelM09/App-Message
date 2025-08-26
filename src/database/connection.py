import psycopg2
from decouple import config

def get_connection():
    try:
        connection = psycopg2.connect(
            host = config('DB_HOST'),
            user = config('DB_USER'),
            password = config('DB_PASS'),
            database = config('DB_NAME'),
            port = config('DB_PORT'),  
        )
        return connection
    except Exception as e:
        return (f"Error connection: {e}")