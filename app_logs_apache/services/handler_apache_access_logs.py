import json
import re
from rapidfuzz import fuzz
from ..models import ApacheAccessLog
from datetime import datetime
import os
from dateutil import parser
from project.settings import ConfigParseLogs


class AccessLogsToJson:

    def __init__(self):
        super().__init__()
        self.new_lines = []
        self.parse_logs = []

    def run(self):
        self.parse_logs = []
        try:
            self._read_file()
        except PermissionError or IndexError:
            return

    def _read_file(self):
        with open(ConfigParseLogs.PATH_FILE, "r") as f:
            self.new_lines = []
            for line in f:
                self.new_lines.append(line)
            if len(self.new_lines) == 0:
                return
            else:
                return self._parse_file()

    def _parse_file(self):
        for el in self.new_lines:
            ip = re.findall(ConfigParseLogs.MASK_IPV4, el)

            if len(ip) == 0:
                ip = re.findall(ConfigParseLogs.MASK_IPV6_V1, el)
                if len(ip) == 0:
                    ip = re.findall(ConfigParseLogs.MASK_IPV6_V2, el)
            date = str(datetime.strptime(re.findall(
                ConfigParseLogs.MASK_DATE, el)[-1], ConfigParseLogs.MASK_FORMAT_DATE))
            data = re.split(r"] ", el)[-1]

            if len(ip) == 1:
                data = data.replace('\"', '')
                self.parse_logs.append(
                    {"ip": ip[-1], "date": date, "data": data})
                    
        return json.dumps({"data": self.parse_logs})


class ReplayHandler:

    def _get_formatted_latest_record_from_db(self):
        sort_records = ApacheAccessLog.objects.order_by('-pk')
        end_record = sort_records[0]
        end_record_valid = end_record.ip + " " + \
            str(end_record.date) + " " + end_record.data
        return end_record_valid

    def _get_a_formatted_record(self, el: list):
        parse_data_valid = el["ip"] + " " + el["date"] + " " + el["data"]
        return parse_data_valid

    def _get_the_date_of_the_last_entry_in_the_database(self):
        date_update = datetime.fromtimestamp(
            os.stat(ConfigParseLogs.PATH_FILE).st_mtime)
        return date_update

    def _checking_and_temporary_storage_new_data(self):
        new_rows = []
        for el in list(reversed(self.parse_data)):
            if fuzz.ratio(self._get_formatted_latest_record_from_db(), self._get_a_formatted_record(el)) != 100 \
                    and parser.parse(self.parse_data[-1]['date']) > self._get_the_date_of_the_last_entry_in_the_database():
                new_rows.append(el)
            else:
                break
        return new_rows


class HandlerJsonAccessLogs(AccessLogsToJson, ReplayHandler):

    def __init__(self):
        super().__init__()
        self.parse_data: list

    def run(self):
        self._start_reading_logs()
        try:
            self._write_new_data_to_database(
                self._checking_and_temporary_storage_new_data())
        except IndexError:
            self._if_base_is_empty()

    def _start_reading_logs(self):
        parse_json_logs = json.loads(self._read_file())
        self.parse_data = parse_json_logs['data']

    def _write_new_data_to_database(self, data: list):
        if len(data) != 0:
            rever_new_rows = list(reversed(data))
            for el in rever_new_rows:
                self._write_a_record(el)

    def _if_base_is_empty(self):
        for el in self.parse_data:
            self._write_a_record(el)

    def _write_a_record(self, el: dict):
        ApacheAccessLog.objects.create(
            ip=el['ip'], date=el['date'], data=el["data"])
