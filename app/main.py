import os


def get_db_url():
    return os.getenv("DB_URL")
