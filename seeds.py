from connect_db import session
from base_creation import Tutors, Groups, Students, Subjects, Marks
import faker
import random


# fill the database with fake data using faker
# (~30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, up to 20 marks for each student in all subjects)


def seed():
    fake = faker.Faker()
    tutor_quantity = random.randint(3, 5)
    group_quantity = 3
    student_quantity = random.randint(30, 50)
    subject_quantity = random.randint(5, 8)
    for i in range(tutor_quantity):
        tutor = Tutors(name=fake.name())


# clear the database and ids to fill the new data
def clear():
    session.query(Tutors).delete()
    session.query(Groups).delete()
    session.query(Students).delete()
    session.query(Subjects).delete()
    session.query(Marks).delete()
    session.commit()


if __name__ == "__main__":
    clear()
    seed()
    print("Database has been filled with fake data")
