import redis
from decouple import config

def connect():
    try:
        db_host = config('RD_HOST')
        db_port = config('RD_PORT')
        db = config('RD_DB')

        connection = redis.Redis(
            host=db_host,
            port=db_port,
            db=db,
            decode_responses=True
        )
        return connection

    except Exception as error:
        print(f"Error connecting to Redis: {error}")
        return None