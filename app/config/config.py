import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("postgresql+psycopg://postgres:123456@localhost:5432/python_login_db")