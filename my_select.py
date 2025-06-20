from sqlalchemy import select, func, desc, Numeric
from models import Student, Group, Teacher, Subject, Grade


# 1. 5 студентів із найбільшим середнім балом з усіх предметів.
async def select_1(session):
    result = await session.execute(
        select(
            Student.name,
            func.round(func.avg(Grade.value).cast(Numeric), 2).label("avg_grade"),
        )
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
    )
    return result.all()


# 2. Студент із найвищим середнім балом з певного предмета.
async def select_2(session, subject_name: str):
    result = await session.execute(
        select(
            Student.name,
            func.round(func.avg(Grade.value).cast(Numeric), 2).label("avg_grade"),
        )
        .join(Grade)
        .join(Subject)
        .where(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
    )
    return result.first()


# 3. Середній бал у групах з певного предмета.
async def select_3(session, subject_name: str):
    result = await session.execute(
        select(
            Group.name,
            func.round(func.avg(Grade.value).cast(Numeric), 2).label("avg_grade"),
        )
        .join(Student, Group.students)
        .join(Grade, Student.grades)
        .join(Subject)
        .where(Subject.name == subject_name)
        .group_by(Group.id)
        .order_by(Group.name)
    )
    return result.all()


# 4. Середній бал на потоці (по всій таблиці оцінок).
async def select_4(session):
    result = await session.execute(
        select(func.round(func.avg(Grade.value).cast(Numeric), 2))
    )
    return result.scalar_one()


# 5. Які курси читає певний викладач.
async def select_5(session, teacher_name: str):
    result = await session.execute(
        select(Subject.name).join(Teacher).where(Teacher.name == teacher_name)
    )
    return [row[0] for row in result]


# 6. Список студентів у певній групі.
async def select_6(session, group_name: str):
    result = await session.execute(
        select(Student.name)
        .join(Group)
        .where(Group.name == group_name)
        .order_by(Student.name)
    )
    return [row[0] for row in result]


# 7. Оцінки студентів у окремій групі з певного предмета.
async def select_7(session, group_name: str, subject_name: str):
    result = await session.execute(
        select(Student.name, Grade.value, Grade.date_received)
        .join(Group, Student.group)
        .join(Grade, Student.grades)
        .join(Subject, Grade.subject)
        .where(Group.name == group_name)
        .where(Subject.name == subject_name)
        .order_by(Student.name)
    )
    return result.all()


# 8. Середній бал, який ставить певний викладач зі своїх предметів.
async def select_8(session, teacher_name: str):
    result = await session.execute(
        select(func.round(func.avg(Grade.value).cast(Numeric), 2).label("avg_grade"))
        .join(Subject, Grade.subject)
        .join(Teacher, Subject.teacher)
        .where(Teacher.name == teacher_name)
    )
    return result.scalar_one()


# 9. Список курсів, які відвідує певний студент.
async def select_9(session, student_name: str):
    result = await session.execute(
        select(Subject.name)
        .join(Grade, Subject.grades)
        .join(Student, Grade.student)
        .where(Student.name == student_name)
        .distinct()
    )
    return [row[0] for row in result]


# 10. Курси, які певному студенту читає певний викладач.
async def select_10(session, student_name: str, teacher_name: str):
    result = await session.execute(
        select(Subject.name)
        .join(Teacher)
        .join(Grade)
        .join(Student)
        .where(Student.name == student_name)
        .where(Teacher.name == teacher_name)
        .distinct()
    )
    return [row[0] for row in result]
