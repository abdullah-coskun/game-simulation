from rest_framework.serializers import ModelSerializer, SerializerMethodField

from score.models import Score


class ScoreSerializer(ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


'''    def create(self, validated_data):
        a=self.request.user
        username = validated_data.get("username")
        points = validated_data.get("points")
        user_obj = Score(
            user_id=username,
            points=points,
        )
        for i in validated_data.get("fields"):
            user_obj.fields.add(i)
        user_obj.save()
        return user_obj'''