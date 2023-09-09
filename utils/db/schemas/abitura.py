from sqlalchemy import Column, BigInteger, String, sql

from utils.db.db_gino import TimedBaseModel


class Abitura(TimedBaseModel):
    __tablename__ = "abiturients"

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(100))
    education = Column(String(50))
    preferences = Column(String(200))
    specialitys = Column(String(200))

    query: sql.select