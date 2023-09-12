from sqlalchemy import Column, BigInteger, String, sql, Numeric

from utils.db.db_gino import TimedBaseModel


class Spo(TimedBaseModel):
    __tablename__ = "Spo"

    name = Column(String(200), primary_key=True)

    budget_places = Column(String(100))
    form_of_education = Column(String(50))
    period_of_study = Column(String(100))
    price = Column(String(50))


    query: sql.select