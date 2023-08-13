#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Index, String, create_engine, desc, asc, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# 1. ✅ Develop a student schema: name, email, grade, birthday(year,month,day)
# 2. ✅ Create a new student record and add it to the database
# 3. ✅ Query all students. 
# 4. ✅ Query all students by name.
# 5. ✅ Query all students by name, and order by name. 
# 6. ✅ Query all students by name, order by name, descending.
# 7. ✅ Limit student query to 1 result
# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
# 9. ✅ Filter student query results by name
# 10. ✅ Update the student data for a single column. 
# 11. ✅ Delete a student database entry/row. 

class Student(Base):
    __tablename__ = 'students'
    Index('index_name', 'name')
# 1. ✅ Develop a student schema: name, email, grade, birthday(year,month,day)
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())
    
    def __repr__(self):
        return f"\n Student {self.id}: "\
            + f"{self.name} "\
            + f"Grade: {self.grade}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


# 3. ✅ Query all students. 
students = session.query(Student)
print([student for student in students])

students = session.query(Student).all()
print(students)


# 4. ✅ Query all students by name. 
students = session.query(Student.name).all()
print(students)

# 5. ✅ Query all students by name, and order by name. 
students = session.query(Student.name).order_by(Student.name).all()
print(students)

# 6. ✅ Query all students by name, order by name, descending.
students = session.query(Student.name).order_by(desc(Student.name)).all()
print(students)

# 7. ✅ Limit student query to 1 result
oldest_student = session.query(Student.name, Student.birthday).order_by(desc(Student.birthday)).limit(2).all()
print(oldest_student)

# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
student_count = session.query(func.count(Student.id)).first()
print(student_count)

# 9. ✅ Filter student query results by name
query = session.query(Student).filter(Student.name.like('%Thompson%'), Student.grade ==7).all()
print(query)

# 10. ✅ Update the student data for a single column.
for student in session.query(Student):
    student.grade += 1

    session.commit()

    print([(student.name, student.grade) for student in session.query(Student)])

# 10. ✅ Update the student data for a single column.
session.query(Student).update({Student.grade: Student.grade+1})

print([(
    student.name,
    student.grade
) for student in session.query(Student)])

# 11. ✅ Delete a student database entry/row. 
query = session.query(Student).filter(Student.name.like("%Albert%"))
albert_einstein = query.first()
print(albert_einstein)

session.delete(albert_einstein)
session.commit()

albert_einstein = query.first()
print("Hopefully is None: ", albert_einstein)

# 2. ✅ Create a new student record and add it to the database
# albert_einstein = Student (
#     name="Albert Einstein",
#     email="albert.einstein@flatironschool.com",
#     grade=4,
#     birthday = datetime(
#         year=1945,
#         month=11,
#         day=11
#     )
# )


# 2. ✅ Create a new student record and add it to the database
# /////////////////////////////////////////////////////////
# joe_stee = Student (
#     name="Joe Stee",
#     email="joe.stee@flatironschool.com",
#     grade=4,
#     birthday = datetime(
#         year=1995,
#         month=2,
#         day=12
#     )
# )

# crab_shack = Student (
#     name="Crab Shack",
#     email="crab_shack@flatironschool.com",
#     grade=4,
#     birthday = datetime(
#         year=1975,
#         month=9,
#         day=3
#     )
# )

# session.bulk_save_objects([joe_stee, crab_shack])
# session.commit()
# print(f"New student ID is {joe_stee.id}")
# print(f"New student ID is {crab_shack.id}")
# ///////////////////////////////////////////////////////////////





# query = session.query(Student).filter(Student.name.like("%Albert%"))
# albert_einstein = query.first()

# session.delete(albert_einstein)
# session.commit()

# albert_einstein = query.first()
# print("Hopefully is None: ", albert_einstein)

