from typing import Optional
from sqlmodel import Field, SQLModel, create_engine

class Alert(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    alert_type: str
    schedule: str


engine = create_engine("sqlite:///alerts.db", echo=True)

def create_alerts_table() -> bool:
    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        print(e)
        return False
    return True