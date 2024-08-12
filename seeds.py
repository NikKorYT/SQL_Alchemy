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
        session.add(tutor)
    for i in range(group_quantity):
        group = Groups(group_name=fake.word())
        session.add(group)
    for i in range(student_quantity):
        student = Students(
            student_name=fake.name(), group_id=random.randint(1, group_quantity)
        )
        session.add(student)
    for i in range(subject_quantity):
        subject = Subjects(subject_name=fake.word(), tutor_id=random.randint(1, tutor_quantity))
        session.add(subject)
    # for each student generate random quantity of marks up to 20 in all subjects
    for student in session.query(Students).all():
        total_marks = random.randint(1, 20)
        subjects = session.query(Subjects).all()
        subject_count = len(subjects)

        marks_per_subject = [0] * subject_count

        for _ in range(total_marks):
            subject_index = random.randint(0, subject_count - 1)
            marks_per_subject[subject_index] += 1

        for subject_index, marks in enumerate(marks_per_subject):
            for _ in range(marks):
                mark = Marks(
                    student_id=student.student_id,
                    subject_id=subjects[subject_index].subject_id,
                    mark=random.randint(1, 100),
                    time=fake.date_this_year(),
                )
                session.add(mark)
    # Commit all data at once
    session.commit()


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
