import grpc
import app.schemas.alert.alert_pb2 as alert_pb2
import app.schemas.alert.alert_pb2_grpc as alert_pb2_grpc
from app.crud import get_alerts

class AlertServer(alert_pb2_grpc.AlertTypeControllerServicer):
    async def UpdateAlertTypeSchedule(self, request: alert_pb2.AlertTypeScheduleRequest, context: grpc.aio.ServicerContext):
        print(request)
        return alert_pb2.AlertTypeScheduleResponse(
            response=alert_pb2.AlertTypeScheduleResponse.Response.OK,
            message="Schedule updated successfully"
        )

    async def ListAlertTypeSchedule(self, request: alert_pb2.ListAlertTypeScheduleRequest, context: grpc.aio.ServicerContext):
        alert_type_list = request.alert_type

        response_list = []
        for alert in alert_type_list:
            alert_db_obj = get_alerts(alert)
            if alert_db_obj:
                response_list.append(alert_db_obj.schedule)

        return alert_pb2.ListAlertTypeScheduleResponse(
            schedule=response_list
        )