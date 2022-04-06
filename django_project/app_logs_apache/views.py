from django.contrib import admin
from rest_framework import generics
from .models import ApacheAccessLog
from daterange.filters import DateRangeFilter
from .services.serializers import ApacheAccessLogSerializer
from django_filters import rest_framework as filters
from .services.filters import ApacheAccessLogFilter


class ApacheAccessLogList(generics.ListAPIView):
    serializer_class = ApacheAccessLogSerializer
    queryset = ApacheAccessLog.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ApacheAccessLogFilter


class ApacheAccessLogAdmin(admin.ModelAdmin):
    model = ApacheAccessLog
    list_display = ("ip", "date", "data")
    list_filter = (("date", DateRangeFilter), "ip")
    search_fields = ("ip", "date", "data")
    change_list_template = "admin/daterange/change_list.html"
    date_hierarchy = 'date'
