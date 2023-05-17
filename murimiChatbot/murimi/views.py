from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
import csv
import os
from django.http import JsonResponse
from . import datasets
from django.conf import settings

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# from .serializers import farming_practices_view
# from .models import Province, Crop,Practice
from .models import info

info =info


# def farming_practices_view(request, province_name, crop_name):
#     try:
#         province = get_object_or_404(Province, name=province_name)
#         crop = get_object_or_404(Crop, name=crop_name)
        
#         if request.method == 'GET':
#             farming_practices = FarmingPractice.objects.filter(province=province, crop=crop)
#             practices_list = [practice.practice for practice in farming_practices]
#             response_data = {
#                 'province': province.name,
#                 'crop': crop.name,
#                 'farming_practices': practices_list
#             }
#             return JsonResponse(response_data)

#         elif request.method == 'POST':
#             practice = request.POST.get('practice')
#             if practice:
#                 FarmingPractice.objects.create(province=province, crop=crop, practice=practice)
#                 return JsonResponse({'success': 'Farming practice added successfully'})
#             else:
#                 return JsonResponse({'error': 'Invalid farming practice'}, status=400)

#         elif request.method == 'PUT':
#             new_practice = request.PUT.get('practice')
#             farming_practice = get_object_or_404(FarmingPractice, province=province, crop=crop)
#             farming_practice.practice = new_practice
#             farming_practice.save()
#             return JsonResponse({'success': 'Farming practice updated successfully'})

#         elif request.method == 'DELETE':
#             farming_practice = get_object_or_404(FarmingPractice, province=province, crop=crop)
#             farming_practice.delete()
#             return JsonResponse({'success': 'Farming practice deleted successfully'})

#     except (Province.DoesNotExist, Crop.DoesNotExist):
#         return JsonResponse({'error': 'Province or crop not found'}, status=404)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# class DatasetView(APIView):
#     def get(self, request, format=None):
#         # Load your dataset and convert it into Python objects
#         dataset = load_dataset()
        
#         # Serialize the dataset
#         serializer = DatasetSerializer(dataset, many=True)
        
#         return Response(serializer.data)


def info_list(request):
    # Fetch data from the info table
    info_queryset = info.objects.all()

    # Prepare combined data
    combined_data = []

    # Add data from the info table
    for information in info_queryset:
        combined_data.append({
            'label': information.label,
            'humidity': information.humidity,
            'ph': information.ph,
            'rainfall': information.rainfall,
            'temperature': information.temperature,
        })

    # Get the path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'info.csv')

    # Read data from the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            combined_data.append({
                'label': row['label'],
                'humidity': row['humidity'],
                'ph': row['ph'],
                'rainfall': row['rainfall'],
                'temperature': row['temperature'],
            })

    return JsonResponse(combined_data, safe=False)
