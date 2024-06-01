from .models import CostModel
from rest_framework import serializers

class CostSerializer(serializers.ModelSerializer):
	class Meta:
		model = CostModel
		fields = "__all__"