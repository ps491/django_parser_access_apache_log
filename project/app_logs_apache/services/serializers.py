from rest_framework import serializers
from ..models import ApacheAccessLog


class ApacheAccessLogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ApacheAccessLog
        fields = "__all__"
