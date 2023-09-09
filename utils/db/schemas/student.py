from sqlalchemy import Column, BigInteger, String, sql

from utils.db.db_gino import TimedBaseModel


class Student(TimedBaseModel):
    __tablename__ = "students"

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    education = Column(String(50))
    form = Column(String(50))
    curs = Column(BigInteger)
    speciality = Column(String(100))

    query: sql.select