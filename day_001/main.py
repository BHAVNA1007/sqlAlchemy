from sqlalchemy import text
from database import engine

connection = engine.connect()
print("database connected successfully")

result = connection.execute(text("select database()"))
print(result.fetchone())
connection.close()