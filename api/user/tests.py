from django.test import TestCase, RequestFactory
from django.urls import reverse
from tastypie.test import ResourceTestCaseMixin

# Create your tests here.
from user.models import MyUser
import json

from user.views import UserLoginAPIView


class LoginandProfileTest(ResourceTestCaseMixin, TestCase):

    def test_fields(self):
        item = MyUser()
        item.display_name = "disp_name"
        item.username = "disp_name"
        item.save()
        record = MyUser.objects.get(display_name='disp_name')
        self.assertEqual(item, record)
        url = '/user/login'
        data = {
            'username': 'disp_name',
        }
        response = self.client.post(url, data, format='json')
        self.assertValidJSONResponse(response)
        token = response.data['token']
        auth = 'JWT {0}'.format(token)
        resp = self.api_client.get('/user/profile', HTTP_AUTHORIZATION=auth, format='json')
        self.assertValidJSONResponse(resp)


class UserTest(TestCase):

    def create_user(self, display_name="disp_name"):
        return MyUser.objects.create(display_name=display_name)

    def test_user(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, MyUser))
        self.assertEqual(user.__str__(), user.display_name)


class LeaderBoardTest(ResourceTestCaseMixin, TestCase):

    def test_get_api_json(self):
        resp = self.api_client.get('/leaderboard', format='json')
        self.assertValidJSONResponse(resp)


class LeaderBoardCountryTest(ResourceTestCaseMixin, TestCase):

    def test_get_api_json(self):
        resp = self.api_client.get('/leaderboard/tr', format='json')
        self.assertValidJSONResponse(resp)
