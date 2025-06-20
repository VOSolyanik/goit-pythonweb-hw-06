import asyncio
import random
from faker import Faker
from datetime import date
from connect import Session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

SUBJECT_NAMES = [
    "Math",
    "Biology",
    "History",
    "Literature",
    "Physics",
    "Chemistry",
    "Philosophy",
    "Programming",
]


def create_groups():
    return [Group(name=f"Group-{i+1}") for i in range(3)]


def create_teachers():
    return [Teacher(name=fake.name()) for _ in range(random.randint(3, 5))]


def create_subjects(teachers):
    subjects_sample = random.sample(
        SUBJECT_NAMES, k=random.randint(5, len(SUBJECT_NAMES))
    )
    return [
        Subject(name=subject_name, teacher=random.choice(teachers))
        for subject_name in subjects_sample
    ]


def create_students(groups):
    return [
        Student(name=fake.name(), group=random.choice(groups))
        for _ in range(random.randint(30, 50))
    ]


def create_grades(students, subjects):
    grades = []
    for student in students:
        subjects_sample = random.sample(subjects, k=random.randint(3, len(subjects)))
        grade_counter = 0
        for subject in subjects_sample:
            if grade_counter >= 20:
                break
            # Generate 5–20 grades for each student-subject pair
            for _ in range(random.randint(5, 20)):
                if grade_counter >= 20:
                    break
                value = random.randint(60, 100)
                date_received = fake.date_between(start_date="-6m", end_date="today")
                grade = Grade(
                    value=value,
                    date_received=date_received,
                    student=student,
                    subject=subject,
                )
                grades.append(grade)
                grade_counter += 1
    return grades


async def seed():
    groups = create_groups()
    teachers = create_teachers()
    subjects = create_subjects(teachers)
    students = create_students(groups)
    grades = create_grades(students, subjects)
    async with Session() as session:
        session.add_all(groups)
        session.add_all(teachers)
        session.add_all(subjects)
        session.add_all(students)
        session.add_all(grades)
        await session.commit()
    print("Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed())
