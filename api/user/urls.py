from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^leaderboard/(?P<pk>[a-z]+)', views.UserCountryListAPIView.as_view(), name="leaderboard_country"),
    url(r'^leaderboard', views.UserListAPIView.as_view(), name="leaderboard"),
    url(r'^user/create', views.UserCreateAPIView.as_view(), name="create"),
    url(r'^user/many/', views.UserRegisterManyAPIView.as_view(), name="createmany"),
    url(r'^user/login', views.UserLoginAPIView.as_view(), name="login"),
    url(r'^user/profile/(?P<pk>[0-9a-f-]+)', views.ProfileWithGUIDAPIView.as_view(), name="profile_uuid"),
    url(r'^user/profile', views.ProfileAPIView.as_view(), name="profile"),
]
