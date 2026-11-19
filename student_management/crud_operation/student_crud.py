from sqlalchemy import select
from model.student import Student
from db.db_config import sessionlocal
from sqlalchemy.exc import SQLAlchemyError

def add_students():

    session = sessionlocal()

    try:
        while True:
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            marks = int(input("Enter marks: "))
            
            student = Student(
                s_name=name, 
                s_age=age, 
                s_marks=marks
                )
            session.add(student)
    
            choice = input("Add another student? (yes/no): ")
    
            if choice.lower() != "yes":
                break

        session.commit()
        print("Employees added successfully!")

    except SQLAlchemyError as e:

        session.rollback()
        print("Database error: ", e)

    except ValueError:
        session.rollback()
        print("please enter a valid info")

    finally:
        session.close()            




def view_students():

    session = sessionlocal()

    try:
        stmt = select(Student)

        students = session.scalars(stmt).all()

        if not students:
            print("No student records found")
            return

        print("\n======== STUDENT RECORDS=======")

        # for student in students:

        #     print(f"id: {student.s_id} | Name: {student.s_name} | age: {student.s_age} | marks: {student.s_marks} |" )


        print(f"{'ID':<5} {'Name':<15} {'AGE':<25} {'MARKS':<10}")
        print("-" * 60)
        
        for student in students:
            print(f"{student.s_id:<5} {student.s_name:<15} {student.s_age:<25} {student.s_marks:<10}")    

    finally:
        session.close()        





def update_student():

    session = sessionlocal()

    try:

        Student_id = int(input("Enter student id to update: "))

        stmt = select(Student).where(Student.s_id == Student_id)

        student = session.scalars(stmt).first()

        if student is None:
            print("Student not found")
            return


        print("Student Name: ", student.s_name)
        print("Current Marks: ", student.s_marks)


        new_marks = int(input("Enter new marks: "))

        if new_marks < 0 or new_marks > 100:

            print("Marks muct be between 0 to 100")
            return

        student.s_marks = new_marks
        session.commit()

        print("Marks updated successfully!")

    except ValueError:
        session.rollback()
        print("Please enter a valid number")


    except Exception as e:

        session.rollback()
        print("Error: ", e)

    finally:        
        session.close()






def delete_student():

    session = sessionlocal()

    try:

        student_id = int(input("Enter student Id to delete: "))

        stmt = select(Student).where(Student.s_id == student_id)

        student = session.scalars(stmt).first()

        if student is None:

            print("Student not found")
            return


        session.delete(student)
        session.commit()
        print("Student deleted successfully")

    except ValueError:

        session.rollback()
        print("plz enter a valid student id")

    except Exception as e:       
        session.rollback()
        print("Error: ", e)


    finally:    
        session.close()