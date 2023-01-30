import logging
import asyncio
from app.app import serve
from app.models.alert_models import Alert, engine, create_alerts_table

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    create_alerts_table()
    asyncio.run(serve())
    