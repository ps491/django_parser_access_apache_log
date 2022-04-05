from ..models import ApacheAccessLog
from django_filters import DateFromToRangeFilter, FilterSet


class ApacheAccessLogFilter(FilterSet):
    date = DateFromToRangeFilter()

    class Meta:
        model = ApacheAccessLog
        fields = ['date', 'ip']
