from django.shortcuts import render
from rest_framework.response import Response
from .models import CostModel
from .ser import CostSerializer
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def home(request):
	articles = CostModel.objects.all()
	serializer = CostSerializer(articles, many=True)
	return Response(serializer.data)
