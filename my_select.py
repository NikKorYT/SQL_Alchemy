from sqlalchemy import select, func
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
    print(table)
    
def select_2():
    #
    pass
