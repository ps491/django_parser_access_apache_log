from django.urls import path
from .views import ApacheAccessLogList


urlpatterns = [
    path('apache_logs/', ApacheAccessLogList.as_view()),
]
