from rest_framework.response import Response


class CustomResponseMixin:
    def custom_response(self, data, message, status_code):
        return Response(
            {"status": "success", "message": message, "data": data}, status=status_code
        )
