from django.test import TestCase
from app_logs_apache.models import ApacheAccessLog
from app_logs_apache.services.serializers import ApacheAccessLogSerializer


class ApacheAccessLogSerializerTestCase(TestCase):
    def setUp(self):
        self.attributes = {
            'ip': '111.111.111',
            'date' : '2022-01-01',
            'data': '404',
        }

        self.serializer_data = {
            'ip': '225.255.255',
            'date' : '2022-01-01',
            'data': '404',
        }

        self.logs = ApacheAccessLog.objects.create(**self.attributes)
        self.serializer = ApacheAccessLogSerializer(instance=self.logs)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','ip', 'date','data']))

    def test_ip_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['ip'], self.attributes['ip'])

    def test_date_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['date'], self.attributes['date'])  
        
    def test_data_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['data'], self.attributes['data'])  

    def test_ip_must_be_in_choices(self):
        self.attributes['ip'] = ''
        serializer = ApacheAccessLogSerializer(instance=self.logs, data=self.attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['ip']))

    def test_date_must_be_in_choices(self):
        self.attributes['date'] = ''
        serializer = ApacheAccessLogSerializer(instance=self.logs, data=self.attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['date']))

    def test_data_must_be_in_choices(self):
        self.attributes['data'] = None
        serializer = ApacheAccessLogSerializer(instance=self.logs, data=self.attributes)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['data']))                                      