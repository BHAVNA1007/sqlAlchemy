print("welcome to our first alchemy app")

from db.db_config import engine, Base

from model.employee import Employee

Base.metadata.create_all(engine)

print("Employee table created in database")