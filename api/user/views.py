from django.shortcuts import render

# Create your views here.

from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from user.createmany import UserCreateManyAPIView
from user.models import MyUser
from user.serializers import UserCreateSerializer, UserLoginSerializer, UserListSerializer, UserCreateManySerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.exceptions import ValidationError
from django.db.models import Q


class UserListAPIView(ListAPIView):
    serializer_class = UserCreateSerializer
    queryset = MyUser.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = MyUser.objects.all().order_by("-points")
        a = []
        for index, instance in enumerate(queryset):
            serializer = UserListSerializer(instance)
            data = serializer.data
            data['rank'] = index + 1
            a.append(data)
        return Response(a, status=200)


class UserCountryListAPIView(ListAPIView):

    def get(self, request, *args, **kwargs):
        country = kwargs.get('pk')
        queryset = MyUser.objects.all().order_by("-points")
        a = []
        for index, instance in enumerate(queryset):
            if instance.country == country:
                serializer = UserListSerializer(instance)
                data = serializer.data
                data['rank'] = index + 1
                a.append(data)
        return Response(a, status=200)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = MyUser.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if not request.data.get('display_name'):
            raise ValidationError({'detail': 'You have to give display name'})
        data['username'] = data['display_name']
        serializer = UserCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        usr_obj = MyUser.objects.filter(id=serializer.data['id']).first()
        serializer = UserListSerializer(usr_obj)
        return Response(serializer.data, status=200)


class UserRegisterManyAPIView(UserCreateManyAPIView):
    serializer_class = UserCreateManySerializer
    queryset = MyUser.objects.all()


class UserLoginAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ProfileAPIView(RetrieveAPIView):
    serializer_class = UserCreateSerializer
    queryset = MyUser.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise ValidationError({"detail":"User is not authorized"})
        user = MyUser.objects.get(id=request.user.id)
        data = UserListSerializer(user).data
        data['rank'] = MyUser.objects.filter(
            Q(points__gt=user.points) | Q(points=user.points, id__lt=user.id)).count() + 1
        return Response(data, status=200)


class ProfileWithGUIDAPIView(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        user = MyUser.objects.filter(user_id=kwargs.get('pk')).first()
        if not user:
            raise ValidationError({'detail': 'This user does not exist'})
        data = UserListSerializer(user).data
        data['rank'] = MyUser.objects.filter(
            Q(points__gt=user.points) | Q(points=user.points, id__lt=user.id)).count() + 1
        return Response(data, status=200)
