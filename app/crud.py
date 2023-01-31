import logging
from typing import Union
from app.models.alert_models import Alert, engine
from sqlmodel import Session, select, Field, SQLModel, insert


def get_alerts(alert_type: str)-> Union[Alert, None]:
    """
        Function that fetch alerts from the database

        Args:
            id (int): id of the alert
        
        Returns:
            Union[Alert, None]: Alert object or None
    """
    with Session(engine) as session:
        alerts = None
        try:
            statement = select(Alert).where(Alert.alert_type == alert_type)
            alerts = session.exec(statement).first()
        except Exception as e:
            logging.error(f"Error in sql: {e}")

        if not alerts:
            return None

        return alerts


def update_alert(a_type, a_schedule):
    with Session(engine) as session:
        try:
            statement = select(Alert).where(Alert.alert_type == a_type)
            results = session.exec(statement)
            alert = results.first()
            if alert:
                logging.info(f"Alert to update: {alert}")
                alert.schedule = a_schedule
            else:
                logging.info(f"Alert to add: {alert}")
                alert = Alert(alert_type=a_type, schedule=a_schedule)
            session.add(alert)
            session.commit()
        except Exception as e:
            logging.error(f"Error in sql: {e}")

