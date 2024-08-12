from sqlalchemy import select, func, distinct
from tabulate import tabulate


from connect_db import session
from base_creation import Tutors, Groups, Students, Subjects, Marks


def select_1():
    # Q1 find five students with the highest average mark in all subjects
    q = (
        session.execute(
            select(Students.student_name, func.avg(Marks.mark).label("average_mark"))
            .join(Marks, Students.student_id == Marks.student_id)
            .group_by(Students.student_name)
            .order_by(func.avg(Marks.mark).desc())
            .limit(5)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nFive students with the highest average mark in all subjects: \n{table}")


def select_2():
    # find the sudent with the highest average grade in one subject(subject_id = 1)
    q = (
        session.execute(
            select(Students.student_name, func.avg(Marks.mark).label("average_mark"))
            .join(Marks, Students.student_id == Marks.student_id)
            .where(Marks.subject_id == 1)
            .group_by(Students.student_name)
            .order_by(func.avg(Marks.mark).desc())
            .limit(1)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nThe student with the highest average mark in subject 1: \n{table}")


def select_3():
    # find an average mark for a group 1 in each subject
    q = (
        session.execute(
            select(Subjects.subject_name, func.avg(Marks.mark).label("average_mark"))
            .join(Marks, Subjects.subject_id == Marks.subject_id)
            .join(Students, Marks.student_id == Students.student_id)
            .where(Students.group_id == 1)
            .group_by(Subjects.subject_name)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nAverage mark for group 1 in each subject: \n{table}")


def select_4():
    # Find an average grade among all students in all subjects
    q = (
        session.execute(select(func.avg(Marks.mark).label("average_mark")))
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nAverage mark among all students in all subjects: \n{table}")


def select_5():
    # Find what subjects does tutor 2 teach
    q = (
        session.execute(
            select(Subjects.subject_name)
            .join(Tutors, Subjects.tutor_id == Tutors.tutor_id)
            .where(Tutors.tutor_id == 2)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nSubjects that tutor 2 teaches: \n{table}")


def select_6():
    # Find a list of students in group 2
    q = (
        session.execute(select(Students.student_name).where(Students.group_id == 2))
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nList of students in group 2: \n{table}")


def select_7():
    # Find marks of group 1 students in subject 4
    # output colums with grades and students names
    q = (
        session.execute(
            select(Students.student_name, Marks.mark)
            .join(Marks, Students.student_id == Marks.student_id)
            .where(Students.group_id == 1)
            .where(Marks.subject_id == 4)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nMarks of group 1 students in subject 4: \n{table}")


def select_8():
    # Find an average mark that tutor 2 gives to his students
    q = (
        session.execute(
            select(func.avg(Marks.mark).label("average_mark"))
            .join(Subjects, Marks.subject_id == Subjects.subject_id)
            .where(Subjects.tutor_id == 2)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nAverage mark that tutor 2 gives to his students: \n{table}")


def select_9():
    # find what subject does student 29 take
    # output columns with course names
    # delete the repeated course names
    q = (
        session.execute(
            select(Subjects.subject_name)
            .join(Marks, Subjects.subject_id == Marks.subject_id)
            .where(Marks.student_id == 29)
        )
        .mappings()
        .all()
    )

    # Format the output as a table
    table = tabulate(q, headers="keys", tablefmt="grid")
    print(f"\nSubjects that student 29 takes: \n{table}")


def select_10():
    # Find a list of subjects that tutor 2 teaches to student 12
    # subjects are not repeated
    # output columns with subject names
    q = (
        session.execute(
            select(distinct(Subjects.subject_name))
            .join(Marks, Subjects.subject_id == Marks.subject_id)
            .where(Marks.student_id == 12)
            .where(Subjects.tutor_id == 2)
        )
        .mappings()
        .all()
    )

    if not q:
        print("Tutor 2 is not teaching any subject to student 12.")
    else:
        # Format the output as a table
        table = tabulate(q, headers="keys", tablefmt="grid")
        print(f"\nSubjects that tutor 2 teaches to student 12: \n{table}")


if __name__ == "__main__":
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
