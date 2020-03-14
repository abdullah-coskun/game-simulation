from django.conf.urls import url

from score import views

urlpatterns = [
    url(r'^submit', views.ScoreCreateSerializer.as_view(), name="create"),
]
