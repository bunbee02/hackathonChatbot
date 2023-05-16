from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .serializers import farming_practices_view
from .models import Province, Crop, FarmingPractice


def farming_practices_view(request, province_name, crop_name):
    try:
        province = get_object_or_404(Province, name=province_name)
        crop = get_object_or_404(Crop, name=crop_name)
        
        if request.method == 'GET':
            farming_practices = FarmingPractice.objects.filter(province=province, crop=crop)
            practices_list = [practice.practice for practice in farming_practices]
            response_data = {
                'province': province.name,
                'crop': crop.name,
                'farming_practices': practices_list
            }
            return JsonResponse(response_data)

        elif request.method == 'POST':
            practice = request.POST.get('practice')
            if practice:
                FarmingPractice.objects.create(province=province, crop=crop, practice=practice)
                return JsonResponse({'success': 'Farming practice added successfully'})
            else:
                return JsonResponse({'error': 'Invalid farming practice'}, status=400)

        elif request.method == 'PUT':
            new_practice = request.PUT.get('practice')
            farming_practice = get_object_or_404(FarmingPractice, province=province, crop=crop)
            farming_practice.practice = new_practice
            farming_practice.save()
            return JsonResponse({'success': 'Farming practice updated successfully'})

        elif request.method == 'DELETE':
            farming_practice = get_object_or_404(FarmingPractice, province=province, crop=crop)
            farming_practice.delete()
            return JsonResponse({'success': 'Farming practice deleted successfully'})

    except (Province.DoesNotExist, Crop.DoesNotExist):
        return JsonResponse({'error': 'Province or crop not found'}, status=404)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialilizer
    

