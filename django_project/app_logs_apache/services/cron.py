#!/usr/bin/env python
from app_logs_apache.services.handler_apache_access_logs import HandlerJsonAccessLogs

def log_handler_apache():
    HandlerJsonAccessLogs().run()