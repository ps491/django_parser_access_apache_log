##!/usr/bin/env python
#import json
#import re
#from rapidfuzz import fuzz
#from ..models import ApacheAccessLog
#from datetime import datetime
#import os
#from dateutil import parser
#from project.settings import ConfigParseLogs
#
#
#class AccessLogsToJson():
#
#    def __init__(self, path_file):
#        super().__init__()
#        self.path_file = path_file
#        self.new_lines = []
#        self.parse_logs = []
#
#    def run(self):
#        self.parse_logs = []
#        try:
#            self._read_file()
#        except PermissionError or IndexError:
#            return
#
#    def _read_file(self):
#        with open(self.path_file, "r") as f:
#            self.new_lines = []
#            for line in f:
#                self.new_lines.append(line)
#            if len(self.new_lines) == 0:
#                return
#            else:
#                return self._parse_file()
#
#    def _parse_file(self):
#        for el in self.new_lines:
#            ip = re.findall(ConfigParseLogs.MASK_IPV4, el)
#            if len(ip) == 0:
#                ip = re.findall(ConfigParseLogs.MASK_IPV6_V1, el)
#                if len(ip) == 0:
#                    ip = re.findall(ConfigParseLogs.MASK_IPV6_V2, el)
#            date = str(datetime.strptime(re.findall(
#                ConfigParseLogs.MASK_DATE, el)[-1], ConfigParseLogs.MASK_FORMAT_DATE))
#            data = re.split(r"] ", el)[-1]
#            if len(ip) == 1:
#                data = data.replace('\"', '')
#                self.parse_logs.append(
#                    {"ip": ip[-1], "date": date, "data": data})
#        return json.dumps({"data": self.parse_logs})
#
#
#
#def log_handler_apache(): 
#    parse_data = start_reading_logs(ConfigParseLogs.PATH_FILE)
#    try:
#        write_new_data_to_database(checking_and_temporary_storage_new_data(
#            data=parse_data, path_file=ConfigParseLogs.PATH_FILE))
#    except IndexError:
#        if_base_is_empty(parse_data)
#
#
#def checking_and_temporary_storage_new_data(data: list, path_file: str):
#    new_rows = []
#    for el in list(reversed(data)):
#        if fuzz.ratio(get_formatted_latest_record_from_db(), get_a_formatted_record(el)) != 100 \
#                and parser.parse(data[-1]['date']) > get_the_date_of_the_last_entry_in_the_database(path_file):
#            new_rows.append(el)
#        else:
#            break
#    return new_rows
#
#
#def get_a_formatted_record(el: list):
#    parse_data_valid = el["ip"] + " " + el["date"] + " " + el["data"]
#    return parse_data_valid
#
#
#def start_reading_logs(path_file: str):
#    logs = AccessLogsToJson(path_file)
#    parse_json_logs = json.loads(logs._read_file())
#    parse_data = parse_json_logs['data']
#    return parse_data
#
#
#def get_the_date_of_the_last_entry_in_the_database(path_file: str):
#    date_update = datetime.fromtimestamp(os.stat(path_file).st_mtime)
#    return date_update
#
#
#def get_formatted_latest_record_from_db():
#    sort_records = ApacheAccessLog.objects.order_by('-pk')
#    end_record = sort_records[0]
#    end_record_valid = end_record.ip + " " + \
#        str(end_record.date) + " " + end_record.data
#    return end_record_valid
#
#
#def write_new_data_to_database(data: list):
#    if len(data) != 0:
#        rever_new_rows = list(reversed(data))
#        for el in rever_new_rows:
#            write_a_record(el)
#
#
#def if_base_is_empty(data: list):
#    for el in data:
#        write_a_record(el)
#
#
#def write_a_record(el: dict):
#    ApacheAccessLog.objects.create(
#        ip=el['ip'], date=el['date'], data=el["data"])
#