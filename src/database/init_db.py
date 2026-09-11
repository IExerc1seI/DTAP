from src.database.base import BaseModel
from src.database.session import engine
from src.database.models.test_run_model import TestRunModel 
from src.database.models.test_result_model import TestResultModel

def init_db():
    BaseModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()