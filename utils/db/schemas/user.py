from sqlalchemy import Column, BigInteger, String, sql

from utils.db.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(50))
    username = Column(String(50))
    status = Column(String(50))
    role = Column(String(50))

    query: sql.select