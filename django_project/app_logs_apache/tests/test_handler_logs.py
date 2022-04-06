from dataclasses import dataclass
from datetime import datetime
import json
from django.test import TestCase
from app_logs_apache.services.handler_apache_access_logs import AccessLogsToJson, HandlerJsonAccessLogs
from app_logs_apache.models import ApacheAccessLog


@dataclass(frozen=True)
class ConfigParseLogs:
    PATH_FILE: str = r"./access.log"
    MASK_IPV4: str = r"^\d+[.]\d+[.]\d+"
    MASK_IPV6_V1: str = r"^\d+[:]\d+[:]\d+"
    MASK_IPV6_V2: str = r"::\d+"
    MASK_DATE: str = r"\d+[/]\D+[/]\d+[:]\d+[:]\d+[:]\d+ [+]\d+\d+\d+\d+"
    MASK_FORMAT_DATE: str = '%d/%b/%Y:%H:%M:%S +%f'


class AccessLogsToJsonTestCase(TestCase):

    
    def test_parse_json_get_data(self):
        request = AccessLogsToJson()._read_file()
        parse_json = json.loads(request)
        self.assertTrue(parse_json)
        key_json = list(parse_json.keys())[0]
        self.assertEquals(key_json, 'data')

    def test_parse_json_get_ip(self):
        request = AccessLogsToJson()._read_file()
        key_json = list(json.loads(request)['data'][0].keys())[0]
        self.assertEquals(key_json, 'ip')

    def test_parse_json_get_date(self):
        request = AccessLogsToJson()._read_file()
        key_json = list(json.loads(request)['data'][0].keys())[1]
        self.assertEquals(key_json, 'date')     

    def test_parse_json_get_data_data(self):
        request = AccessLogsToJson()._read_file()
        key_json = list(json.loads(request)['data'][0].keys())[2]
        self.assertEquals(key_json, 'data')  

    def test_parse_json_check_not_empty_data(self):
        request = AccessLogsToJson()._read_file()
        parse_json = json.loads(request)
        data_value = list(parse_json.values())[0]
        self.assertTrue(data_value)

    def test_parse_json_check_not_empty_ip(self):
        request = AccessLogsToJson()._read_file()
        parse_json = json.loads(request)['data'][0]
        ip_value = list(parse_json.values())[0]
        self.assertTrue(ip_value)        

    def test_parse_json_check_not_empty_date(self):
        request = AccessLogsToJson()._read_file()
        parse_json = json.loads(request)['data'][0]
        date_value = list(parse_json.values())[1]
        self.assertTrue(date_value)         

    def test_parse_json_check_not_empty_data_data(self):
        request = AccessLogsToJson()._read_file()
        parse_json = json.loads(request)['data'][0]
        data_data_value = list(parse_json.values())[2]
        self.assertTrue(data_data_value)    


class HandlerJsonAccessLogsTestCase(TestCase):

    def setUp(self):
        HandlerJsonAccessLogs().run()

    def test_run_get_ip(self):   
        log = ApacheAccessLog.objects.get(id=1) 
        self.assertTrue(log.ip)

    def test_run_get_date(self):   
        log = ApacheAccessLog.objects.get(id=1) 
        self.assertTrue(log.date)  

    def test_run_get_data(self):
        log = ApacheAccessLog.objects.get(id=1) 
        self.assertTrue(log.data) 


    def test_run_check_type_ip(self):   
        log = ApacheAccessLog.objects.get(id=1) 
        assert isinstance(log.ip, str)

    def test_run_check_type_date(self):   
        log = ApacheAccessLog.objects.get(id=1) 
        assert isinstance(log.date, datetime) 

    def test_run_check_type_data(self):
        log = ApacheAccessLog.objects.get(id=1) 
        assert isinstance(log.data, str)                                