from sqlalchemy import Column, BigInteger, String, sql, Numeric

from utils.db.db_gino import TimedBaseModel


class Vo_ozfo(TimedBaseModel):
    __tablename__ = "Vo_ozfo"

    name = Column(String(200), primary_key=True)

    budget_places = Column(String(100))
    form_of_education = Column(String(50), default="Очно-Заочная")
    period_of_study = Column(String(100))
    price = Column(String(50))
    examination = Column(String(200))
    entrance_test = Column(String(200))
    comment = Column(String(1000))


    query: sql.select