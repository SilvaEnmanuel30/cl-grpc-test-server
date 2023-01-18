import logging
import asyncio
from app.app import serve

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())