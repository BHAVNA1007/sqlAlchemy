

from db.db_config import engine, Base
from model.employee import Employee

from db.db_config import sessionlocal


# Base.metadata.create_all(engine)

# employee add
#emp = Employee(name = "deepika", email="dipu@gmail.com", salary= 90000)
# emp = Employee(name = "rashmika", email="rashmika@gmail.com", salary= 100000)



session = sessionlocal()

# print all data (fetch)
# employees = session.query(Employee).all()
# for emp in employees:
#     print(emp.id, emp.name, emp.salary)
# session.close()    
# print("table entry will be print if everything is right")







#fetch by id one emp

# employee = session.query(Employee).filter(Employee.id==1).first()
# if employee:
#     print(employee.name, employee.email)
# else:
#     print("Employee not found")

# session.close()
# print("table entry one employee will be print if everything is right")    






# employee = session.query(Employee).filter(Employee.email=="dipu@gmail.com").first()
# if employee:
#     print(employee.name, employee.email)
# else:
#     print("Employee not found")

# session.close()
# print("table entry one employee will be print if everything is right") 





# update info  old approch
# employee = session.query(Employee).filter(Employee.id==1).first()
# if employee:
#     employee.salary = 100000
#     session.commit()
#     print("employee salary updated successfully")
# else:
#     print("Employee not found")

# session.close()
# print("table entry one employee will be print if everything is right")    





# modern sqlalchemy select syntax

from sqlalchemy import select
# stmt = select(Employee)
# employees = session.scalars(stmt).all()
# for emp in employees:
#     print(emp.id, emp.name, emp.salary)

# print("using modern way")    









# stmt = select(Employee).where(Employee.id == 1)
# employee = session.scalars(stmt).first()
# if employee:
#     print(employee.id, employee.name, employee.salary)
# else:
#     print("employee not found")    

# print("using modern way")    







# stmt = select(Employee).where(Employee.salary>1, Employee.salary>80000)
# employees = session.scalars(stmt).all()
# for emp in employees:
#     print(emp.id, emp.name, emp.salary)

# print("using modern way")   



