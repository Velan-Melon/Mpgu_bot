from sqlalchemy import Column, BigInteger, String, sql, Numeric

from utils.db.db_gino import TimedBaseModel


class Spo(TimedBaseModel):
    __tablename__ = "Spo"

    name = Column(String(200), primary_key=True)

    budget_places_9 = Column(String(100))
    form_of_education_9 = Column(String(50))
    period_of_study_9 = Column(String(100))
    price_9 = Column(String(50))

    budget_places_11 = Column(String(100))
    form_of_education_11 = Column(String(50))
    period_of_study_11 = Column(String(100))
    price_11 = Column(String(50))


    query: sql.select