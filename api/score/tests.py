from django.test import TestCase, RequestFactory
from django.urls import reverse
from tastypie.test import ResourceTestCaseMixin

# Create your tests here.
from user.models import MyUser
import json

# Create your tests here.

class ScoreSubmit(ResourceTestCaseMixin, TestCase):

    def test_fields(self):
        item = MyUser()
        item.display_name = "disp_name1"
        item.username = "disp_name1"
        item.save()
        url = '/user/login'
        data = {
            'username': 'disp_name1',
        }
        response = self.client.post(url, data, format='json')
        self.assertValidJSONResponse(response)
        token = response.data['token']
        url_submit = '/score/submit'
        data_submit = {
            'points': 4,
        }
        auth = 'JWT {0}'.format(token)
        resp = self.api_client.post(url_submit,data=data_submit, HTTP_AUTHORIZATION=auth, format='json')
        self.assertValidJSONResponse(resp)
        data_submit_2 = {
            'points': 5,
        }
        resp = self.api_client.post(url_submit, data=data_submit_2, HTTP_AUTHORIZATION=auth, format='json')
        self.assertValidJSONResponse(resp)
        record = MyUser.objects.get(display_name='disp_name1')
        self.assertEqual(9, record.points)
