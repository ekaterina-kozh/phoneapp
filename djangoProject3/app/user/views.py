from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class UserByToken(APIView):

    def post(self, request, format=None):
        print(request.user)
        data = {
            "id": str(request.user.id),
            "username": str(request.user.username),
            "is_staff": str(request.user.is_staff)
        }
        return Response(data, status=status.HTTP_201_CREATED)
