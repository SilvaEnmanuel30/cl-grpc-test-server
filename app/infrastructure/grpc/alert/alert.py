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

    async def ListAlertTypeSchedule(self, request: alert_pb2.ListAlertTypeScheduleRequest, context: grpc.aio.ServicerContext):
        alert_type_list = request.alert_type
        schedule = {
            "monday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "tuesday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "wednesday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "thursday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "friday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "saturday": {
                "start_time": "09:00",
                "end_time": "17:00"
            },
            "sunday": {
                "start_time": "09:00",
                "end_time": "17:00"
            }
        }

        alert_type_schedule = []
        for alert_type in alert_type_list:
            # Lectura Yaml
            alert_type_schedule.append(schedule)

        response = alert_pb2.ListAlertTypeScheduleResponse(
            schedule= alert_type_schedule)
        return response