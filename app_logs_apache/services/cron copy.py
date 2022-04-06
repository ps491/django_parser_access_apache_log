##!/usr/bin/env python
#import json
#import re
#from rapidfuzz import fuzz 
#from ..models import ApacheAccessLog
#from datetime import datetime
#import os
#from dateutil import parser
#
#global lines
#lines = []
#
#class ParserAccessLog():
#
#    def __init__(self, path_file):
#        super().__init__()
#        self.path_file = path_file
#        self.new_lines = []
#        self.parse_logs = []
#
#
#    def _read_file(self):
#        self.parse_logs = []
#        try:
#            with open(self.path_file, "r") as frb:
#                self.new_lines = []
#                for idx, l in enumerate(frb):
#                    if len(lines) == 0:
#                        self.new_lines.append(l)
#                    else:
#                        try:
#                            if fuzz.ratio(l, lines[0]) == 100:
#                                break
#                            else:
#                                self.new_lines.append(l)
#                        except IndexError:
#                            break
#                if len(self.new_lines) == 0:
#                    return
#                else:
#                    return self._parse_file()
#
#        except PermissionError or IndexError:
#            return
#
#    def _parse_file(self):
#        for el in self.new_lines:
#            ip = re.findall(r"^\d+[.]\d+[.]\d+", el)
#            if len(ip) == 0:
#                ip = re.findall(r"^\d+[:]\d+[:]\d+", el)
#                if len(ip) == 0:
#                    ip = re.findall(r"::\d+", el)
#            #date = str(datetime.strptime(re.findall(r"\d+[/]\D+[/]\d+[:]\d+[:]\d+[:]\d+", el)[-1], '%d/%b/%Y:%H:%M:%S'))
#            date = str(datetime.strptime(re.findall(r"\d+[/]\D+[/]\d+[:]\d+[:]\d+[:]\d+ [+]\d+\d+\d+\d+", el)[-1], '%d/%b/%Y:%H:%M:%S +%f'))
#            data = re.split(r"] ", el)[-1]
#            if len(ip) == 1:
#                data = data.replace('\"', '')
#                self.parse_logs.append({"ip": ip[-1], "date": date, "data": data})
#        for idx, el in enumerate(self.new_lines):
#            lines.insert(idx, el)
#
#        return json.dumps({"data": self.parse_logs})
#
#
#
#
#
#
#
#def my_scheduled_job():
#    new_rows = []
#    path_file = r"/var/log/apache2/access.log"
#    logs = ParserAccessLog(path_file)
#    date_update = datetime.fromtimestamp(os.stat(path_file).st_mtime)
#    parse_json_logs = json.loads(logs._read_file())
#    parse_data = parse_json_logs['data']
#
#    try:
#        sort_records = ApacheAccessLog.objects.order_by('-pk')
#        end_record = sort_records[0]
#        end_record_valid = end_record.ip + " " + str(end_record.date)  + " " + end_record.data     
#        rever_parse_data = list(reversed(parse_data))
#        for idx, el in enumerate(rever_parse_data):
#            parse_data_valid = el["ip"] + " " + el["date"]+ " " + el["data"]
#
#            if fuzz.ratio(end_record_valid, parse_data_valid) !=100 and  parser.parse(parse_data[-1]['date']) > date_update:
#                new_rows.append(el)
#                #ApacheAccessLog.objects.create(ip=el['ip'] , date=el['date'], data=el['data'])
#            else:
#                break
#        if len(new_rows) != 0:
#            rever_new_rows = list(reversed(new_rows))
#            for el in rever_new_rows:
#                ApacheAccessLog.objects.create(ip=el['ip'] , date=el['date'], data=el['data'])
#    except IndexError:
#        for idx, el in enumerate(parse_data):
#            ApacheAccessLog.objects.create(ip=el['ip'] , date=el['date'], data=el["data"])
#      
