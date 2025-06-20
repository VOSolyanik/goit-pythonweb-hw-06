# goit-pythonweb-hw-06

## Setup

### 1. Install project dependencies

-  `poetry install`

### 2. Run local Postgres DB in Docker

- `docker run --name student-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres` where `mysecretpassword` is your custom password. Other params could be changed too.

### 3. Create .env file

- You need to create `.env` file from sample `.env.sample` and update according to your params in Docker command that runs Postgres instance

### 4. Run DB migrations

- `poetry run alembic upgrade head`

### 5. Run seeding

- `poetry run python seed.py` to fill DB with test data

### 6. Run

- `poetry run python main.py` to check `my_select.py` result.

## Results:

```
2025-06-21 00:08:15,955 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2025-06-21 00:08:15,955 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-06-21 00:08:15,957 INFO sqlalchemy.engine.Engine select current_schema()
2025-06-21 00:08:15,957 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-06-21 00:08:15,959 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2025-06-21 00:08:15,959 INFO sqlalchemy.engine.Engine [raw sql] ()
2025-06-21 00:08:15,960 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-06-21 00:08:15,964 INFO sqlalchemy.engine.Engine SELECT students.name, round(CAST(avg(grades.value) AS NUMERIC), $1::INTEGER) AS avg_grade 
FROM students JOIN grades ON students.id = grades.student_id GROUP BY students.id ORDER BY avg_grade DESC 
 LIMIT $2::INTEGER
2025-06-21 00:08:15,964 INFO sqlalchemy.engine.Engine [generated in 0.00013s] (2, 5)
[('Patricia Weiss', Decimal('86.10')), ('Anita Wright', Decimal('85.45')), ('Jasmine James', Decimal('84.10')), ('Teresa Haas', Decimal('83.20')), ('Daniel Pearson', Decimal('82.05'))]
2025-06-21 00:08:15,969 INFO sqlalchemy.engine.Engine SELECT students.name, round(CAST(avg(grades.value) AS NUMERIC), $1::INTEGER) AS avg_grade 
FROM students JOIN grades ON students.id = grades.student_id JOIN subjects ON subjects.id = grades.subject_id 
WHERE subjects.name = $2::VARCHAR GROUP BY students.id ORDER BY avg_grade DESC 
 LIMIT $3::INTEGER
2025-06-21 00:08:15,969 INFO sqlalchemy.engine.Engine [generated in 0.00007s] (2, 'Math', 1)
('Patricia Weiss', Decimal('99.00'))
2025-06-21 00:08:15,973 INFO sqlalchemy.engine.Engine SELECT groups.name, round(CAST(avg(grades.value) AS NUMERIC), $1::INTEGER) AS avg_grade 
FROM groups JOIN students ON groups.id = students.group_id JOIN grades ON students.id = grades.student_id JOIN subjects ON subjects.id = grades.subject_id 
WHERE subjects.name = $2::VARCHAR GROUP BY groups.id ORDER BY groups.name
2025-06-21 00:08:15,973 INFO sqlalchemy.engine.Engine [generated in 0.00007s] (2, 'Math')
[('Group-1', Decimal('80.57')), ('Group-2', Decimal('79.20')), ('Group-3', Decimal('79.72'))]
2025-06-21 00:08:15,975 INFO sqlalchemy.engine.Engine SELECT round(CAST(avg(grades.value) AS NUMERIC), $1::INTEGER) AS round_1 
FROM grades
2025-06-21 00:08:15,975 INFO sqlalchemy.engine.Engine [generated in 0.00004s] (2,)
79.90
2025-06-21 00:08:15,977 INFO sqlalchemy.engine.Engine SELECT subjects.name 
FROM subjects JOIN teachers ON teachers.id = subjects.teacher_id 
WHERE teachers.name = $1::VARCHAR
2025-06-21 00:08:15,977 INFO sqlalchemy.engine.Engine [generated in 0.00004s] ('Matthew Gray',)
['History', 'Math']
2025-06-21 00:08:15,978 INFO sqlalchemy.engine.Engine SELECT students.name 
FROM students JOIN groups ON groups.id = students.group_id 
WHERE groups.name = $1::VARCHAR ORDER BY students.name
2025-06-21 00:08:15,978 INFO sqlalchemy.engine.Engine [generated in 0.00003s] ('Group-1',)
['Andrew Brennan', 'Cameron Flores', 'Christina Smith', 'Daniel Pearson', 'Dr. Stephanie Tate', 'Jasmine James', 'Kathleen Reynolds', 'Larry Douglas', 'Mary Owen', 'Melissa Lee', 'Michael Lewis', 'Oscar Mullins', 'Patricia Weiss', 'Spencer Pena', 'Teresa Haas', 'Veronica Richardson', 'Victor Garcia']
2025-06-21 00:08:15,985 INFO sqlalchemy.engine.Engine SELECT students.name, grades.value, grades.date_received 
FROM students JOIN groups ON groups.id = students.group_id JOIN grades ON students.id = grades.student_id JOIN subjects ON subjects.id = grades.subject_id 
WHERE groups.name = $1::VARCHAR AND subjects.name = $2::VARCHAR ORDER BY students.name
2025-06-21 00:08:15,985 INFO sqlalchemy.engine.Engine [generated in 0.00008s] ('Group-1', 'Math')
[('Cameron Flores', 97.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 72.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 93.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 67.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 77.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 70.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 99.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 74.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 62.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 73.0, datetime.date(2025, 6, 19)), ('Cameron Flores', 77.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 84.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 77.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 87.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 76.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 97.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 94.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 99.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 91.0, datetime.date(2025, 6, 19)), ('Daniel Pearson', 60.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 97.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 81.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 100.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 77.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 100.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 73.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 95.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 71.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 82.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 84.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 82.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 66.0, datetime.date(2025, 6, 19)), ('Dr. Stephanie Tate', 82.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 98.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 62.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 92.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 90.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 92.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 92.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 63.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 69.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 82.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 83.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 67.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 65.0, datetime.date(2025, 6, 19)), ('Larry Douglas', 78.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 99.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 82.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 98.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 71.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 69.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 70.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 73.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 70.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 71.0, datetime.date(2025, 6, 19)), ('Melissa Lee', 95.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 61.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 60.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 60.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 82.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 78.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 94.0, datetime.date(2025, 6, 19)), ('Michael Lewis', 82.0, datetime.date(2025, 6, 19)), ('Patricia Weiss', 99.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 89.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 88.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 75.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 65.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 90.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 89.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 72.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 83.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 73.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 98.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 72.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 92.0, datetime.date(2025, 6, 19)), ('Teresa Haas', 86.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 94.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 61.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 79.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 69.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 95.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 83.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 75.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 65.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 79.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 78.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 99.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 67.0, datetime.date(2025, 6, 19)), ('Victor Garcia', 72.0, datetime.date(2025, 6, 19))]
2025-06-21 00:08:15,988 INFO sqlalchemy.engine.Engine SELECT round(CAST(avg(grades.value) AS NUMERIC), $1::INTEGER) AS avg_grade 
FROM grades JOIN subjects ON subjects.id = grades.subject_id JOIN teachers ON teachers.id = subjects.teacher_id 
WHERE teachers.name = $2::VARCHAR
2025-06-21 00:08:15,988 INFO sqlalchemy.engine.Engine [generated in 0.00006s] (2, 'James Duncan')
80.13
2025-06-21 00:08:15,990 INFO sqlalchemy.engine.Engine SELECT DISTINCT subjects.name 
FROM subjects JOIN grades ON subjects.id = grades.subject_id JOIN students ON students.id = grades.student_id 
WHERE students.name = $1::VARCHAR
2025-06-21 00:08:15,990 INFO sqlalchemy.engine.Engine [generated in 0.00006s] ('James Booth',)
['History', 'Math']
2025-06-21 00:08:15,991 INFO sqlalchemy.engine.Engine SELECT DISTINCT subjects.name 
FROM subjects JOIN teachers ON teachers.id = subjects.teacher_id JOIN grades ON subjects.id = grades.subject_id JOIN students ON students.id = grades.student_id 
WHERE students.name = $1::VARCHAR AND teachers.name = $2::VARCHAR
2025-06-21 00:08:15,991 INFO sqlalchemy.engine.Engine [generated in 0.00006s] ('James Booth', 'Matthew Gray')
['History', 'Math']
2025-06-21 00:08:15,993 INFO sqlalchemy.engine.Engine ROLLBACK
```
