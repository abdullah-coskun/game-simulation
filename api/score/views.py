from django.shortcuts import render

# Create your views here.

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from score.models import Score
from score.serializers import ScoreSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from user.models import MyUser


class ScoreCreateSerializer(CreateAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise ValidationError("User is not authorized")
        data = request.data
        user = MyUser.objects.get(id=request.user.id)
        data['user_id'] = user.user_id
        serializer = ScoreSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user.points += data['points']
        user.save()
        return Response(serializer.data, status=200)
