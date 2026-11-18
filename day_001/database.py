
import os

from dotenv import load_dotenv
from sqlalchemy.engine import URL
from sqlalchemy import create_engine


load_dotenv()



url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)
engine = create_engine(url, echo = True)

print("sql alchemy engine created successfully")