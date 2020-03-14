from rest_framework.serializers import ModelSerializer, SerializerMethodField

from user.models import MyUser
from rest_framework_jwt.settings import api_settings
from rest_framework.fields import CharField

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {
            "password":
                {"required": False}
        }


class UserListSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            "user_id",
            "display_name",
            "points",
            "country",
        ]


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(write_only=True, required=True)
    user = UserListSerializer(read_only=True)

    class Meta:
        model = MyUser
        fields = [
            'username',
            'token',
            'user',

        ]
        extra_kwargs = {"password":
                            {"write_only": True, "required": False}
                        }

    def validate(self, data):
        user_obj = MyUser.objects.filter(username=data.get("username")).first()
        if not user_obj:
            raise ValidationError({'detail':'Incorrect Credentials'})
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        data["token"] = token
        data["user"] = user_obj
        return data
