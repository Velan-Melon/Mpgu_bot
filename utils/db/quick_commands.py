from asyncpg import UniqueViolationError

from utils.db.db_gino import db
from utils.db.schemas.user import User
from utils.db.schemas.student import Student
from utils.db.schemas.abitura import Abitura



async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str, role="Пользователь"):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status, role=role)
        await user.create()
    except UniqueViolationError:
        print("пользователь не добавлен")


async def select_all_users():
    users = await User.query.gino.all()
    return users

async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def select_username(username):
    user = await User.query.where(User.username == username).gino.first()
    return user

async def check_role():
    role = await User.role
    print(role)
    return role

async def update_role(user_id, new_role):
    user = await select_user(user_id)
    await user.update(role=new_role).apply()

async def add_student(user_id: int):
    try:
        user = Student(user_id=user_id)
        user2 = Abitura(user_id=user_id)
        await user2.delete()
        await user.create()
    except UniqueViolationError:
        print("Студент не добавлен")

async def select_student(user_id):
    user = await Student.query.where(Student.user_id == user_id).gino.first()
    return user

async def update_student_education(user_id, education):
    student = await select_student(user_id)
    await student.update(education=education).apply()

async def update_student_username(user_id, username):
    student = await select_student(user_id)
    await student.update(username=username).apply()

async def update_student_form(user_id, form):
    student = await select_student(user_id)
    await student.update(form=form).apply()

async def update_student_curs(user_id, curs):
    student = await select_student(user_id)
    await student.update(curs=curs).apply()

async def update_student_speciality(user_id, speciality):
    student = await select_student(user_id)
    await student.update(speciality=speciality).apply()


async def add_abiturient(user_id: int):
    try:
        abitur = await select_user(user_id)
        user = Abitura(user_id=user_id, username=abitur.username)
        user2 = Student(user_id=user_id)
        await user2.delete()
        await user.create()

    except UniqueViolationError:
        print("Абитуриент не добавлен")

