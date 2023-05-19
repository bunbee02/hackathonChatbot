from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import serializers


# from rest_frameworks import serializers
from rest_framework import serializers
from .models import Product
from .models import Province, Crop



# def farming_practices_view(request, province_name, crop_name):
#     try:
#         province = get_object_or_404(Province, name=province_name)
#         crop = get_object_or_404(Crop, name=crop_name)
#         farming_practices = FarmingPractice.objects.filter(province=province, crop=crop)

#         practices_list = [practice.practice for practice in farming_practices]
#         response_data = {
#             'province': province.name,
#             'crop': crop.name,
#             'farming_practices': practices_list
#         }
#         return JsonResponse(response_data)
#     except (Province.DoesNotExist, Crop.DoesNotExist):
#         return JsonResponse({'error': 'Province or crop not found'}, status=404)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']
        
        

# class DatasetSerializer(serializers.Serializer):
#     field1 = serializers.CharField()
#     field2 = serializers.IntegerField()
