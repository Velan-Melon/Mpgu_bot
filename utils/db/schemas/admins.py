from sqlalchemy import Column, BigInteger, String, sql

from utils.db.db_gino import TimedBaseModel


class Admins(TimedBaseModel):
    __tablename__ = "admins"

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(100))
    status = Column(String(50))

    query: sql.select