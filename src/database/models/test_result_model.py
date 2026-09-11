from sqlalchemy import Column, Integer, String, DateTime
from src.database.base import BaseModel

class TestResultModel(BaseModel):
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=True)