from django.shortcuts import render
from django.http import JsonResponse
from .corona_static import xray_production
from .serializers import ImageSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
# Create your views here.

@csrf_exempt
def get_corona(request, *args, **kwargs):
	if request.method == 'POST':
		print(request.FILES)
		# data = request.POST
		# image = request.FILES['image']
		# print(request.FILES)
		# image = Image.open(image).convert('RGB')
		# data = xray_production.predict(image)
		# return JsonResponse({'data': data})	
	return JsonResponse({'msg':'GET'})
