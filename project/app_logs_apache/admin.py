from django.contrib import admin
from .models import ApacheAccessLog
from .views import ApacheAccessLogAdmin

admin.site.register(ApacheAccessLog, ApacheAccessLogAdmin)
