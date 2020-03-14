from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

class UserCreateManyAPIView(APIView):
    serializer_class = None

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
