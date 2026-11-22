from db.db_config import sessionlocal, engine, Base
from  sqlalchemy import select
from model.department import Department
from model.employee import Employee


# Base.metadata.create_all(engine)
# print("two tables created with foregin key")



# def  createdepartment():
#     session = sessionlocal()
#     dept = Department(dept_name = "IT")
#     session.add(dept)
#     session.commit()
#     print("department added")

#     session.close()

# createdepartment()



# def createemployee():
    # session = sessionlocal()
# 
    # emp = Employee(name = "deepika", email = "dipu@gmail.com", salary = 9000)
    # emp = Employee(name = "rashmika", email = "rashmi@gmail.com", salary = 8000)
    # dept = session.get(Department, 1)
    # dept.employees.append(emp)
    # session.commit()
    # print("Employee added")
    # session.close()
# 
# createemployee()










def getAllemployees():
    session = sessionlocal()
    stmt = select(Employee)
    result = session.execute(stmt)

    employees = result.scalars().all()

    for emp in  employees:

        print("ID", emp.id)
        print("Name", emp.name)
        print("Email", emp.email)
        print("DID", emp.dept_id)
        print("DNAME", emp.department.dept_name)

    session.close()


getAllemployees()
    





