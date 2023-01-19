from typing import Union
from app.models.alert_models import Alert, engine
from sqlmoel import Session, select, Field, SQLModel


def get_alerts(alert_type: str)-> Union[Alert, None]:
    """
        Function that fetch alerts from the database

        Args:
            id (int): id of the alert
        
        Returns:
            Union[Alert, None]: Alert object or None
    """
    with Session(engine) as session:
        statement = select(Alert).where(Alert.alert_type == alert_type)
        alerts = session.exec(statement).first()

        if not alerts:
            return None

        return alerts