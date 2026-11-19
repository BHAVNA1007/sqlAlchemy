from db.db_config import engine, Base

Base.metadata.create_all(engine)

from crud_operation.student_crud import (
    add_students,
    view_students,
    update_student,
    delete_student
)


while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit") 

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
           add_students()

        case 2:
            view_students()
            break

        case 3:
            update_student()

        case 4:
            delete_student()  

        case _:
            print("invalid choice")       




