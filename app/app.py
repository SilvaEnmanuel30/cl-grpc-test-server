import asyncio
import logging
import os

import grpc
import app.schemas.alert.alert_pb2 as alert_pb2
import app.schemas.alert.alert_pb2_grpc as alert_pb2_grpc
from app.infrastructure.grpc.alert.alert import AlertServer


async def serve() -> None:
    server = grpc.aio.server()
    alert_pb2_grpc.add_AlertTypeControllerServicer_to_server(AlertServer(), server)
    listen_addr = "[::]:" + os.environ.get("SERVER_HOST", "50051")
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
