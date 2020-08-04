from django.shortcuts import render
from django.http import JsonResponse
from .corona_static import xray_production
from .serializers import ImageSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

@csrf_exempt
def get_corona(request, *args, **kwargs):
	'''Takes xray report as an input and preedict weather the patient is corona positive or not
	'''
	if request.method == 'POST':
		data = request.POST
		image = request.FILES['image']
		print(image)
		image = Image.open(image).convert('RGB')
		data = xray_production.predict(image)
		return JsonResponse({'data': data})	
	return JsonResponse({'msg':'GET'})
