import os
from dotenv import load_dotenv

load_dotenv()

dialect = os.getenv('DB_DIALECT', default='mysql')
username = os.getenv('DB_USERNAME', default='root')
password_env = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST', default='127.0.0.1')
port = os.getenv('DB_PORT', default='3306')

def get_db_password(password_env):
    if password_env:
        return f':{password_env}'
    return ''

password = get_db_password(password_env)
DB_URL = f'{dialect}://{username}{password}@{host}:{port}'
