from sqlalchemy import Column, BigInteger, String, sql, Numeric

from utils.db.db_gino import TimedBaseModel


class Vo_zfo(TimedBaseModel):
    __tablename__ = "Vo_zfo"

    name = Column(String(200), primary_key=True)

    budget_places_on_11 = Column(String(100))
    form_of_education_on_11 = Column(String(50), default="Заочная")
    period_of_study_on_11 = Column(String(100))
    price_on_11 = Column(String(50))
    examination_on_11 = Column(String(200))

    budget_places_on_spo = Column(String(100))
    form_of_education_on_spo = Column(String(50), default="Заочная")
    period_of_study_on_spo = Column(String(100))
    price_on_spo = Column(String(50))
    examination_on_spo = Column(String(200))

    budget_places_on_vo = Column(String(100))
    form_of_education_on_vo = Column(String(50), default="Заочная")
    period_of_study_on_vo = Column(String(100))
    price_on_vo = Column(String(50))
    examination_on_vo = Column(String(200))


    query: sql.select