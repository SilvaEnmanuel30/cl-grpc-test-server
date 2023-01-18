import grpc
import app.schemas.alert.alert_pb2 as alert_pb2
import app.schemas.alert.alert_pb2_grpc as alert_pb2_grpc


class AlertServer(alert_pb2_grpc.AlertTypeControllerServicer):
    async def UpdateAlertTypeSchedule(self, request: alert_pb2.AlertTypeScheduleRequest, context: grpc.aio.ServicerContext):
        print(request)
        return alert_pb2.AlertTypeScheduleResponse(
            response=alert_pb2.AlertTypeScheduleResponse.Response.OK,
            message="Schedule updated successfully"
        )
