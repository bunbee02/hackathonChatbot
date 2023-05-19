from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
import cv2
import numpy as np
import csv
import os
from PIL import Image
from django.http import JsonResponse
# from . import datasets
from django.conf import settings
from twilio.base.exceptions import TwilioRestException

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# from .serializers import farming_practices_view
# from .models import Province, Crop,Practice
from .models import info
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = 'AC37cebed5e43eb81f4c0345dda4da8a4d'
auth_token = '104ba6f60c47dcdbaf0291e03d7f219d'
client = Client(account_sid, auth_token)


info =info
from .models import CropDisease
CropDisease =CropDisease

account_sid = 'AC37cebed5e43eb81f4c0345dda4da8a4d'
auth_token = '337348d00cd743158b37ac536c4fa7d9'
client = Client(account_sid, auth_token)

# @csrf_exempt
# def bot(request): 
#     print(request.POST.get('Body', ''))
    # message = request.POST['Body']
    # print(request)
    # print(message)
    # if (message == 'hi'):
    #     try: 
    #         print(message)
    #         client.messages.create(
    #         from_='whatsapp:+14155238886',
    #         body='Welcome to Murimi bot please select the region you are coming',
    #         to='whatsapp:+263713872372'
    #         )
    #     except TwilioRestException as ex: 
    #         print(ex)

    # return HttpResponse("hello")


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




def preprocess_image(image):
    # Read the uploaded image using OpenCV
    img = cv2.imdecode(image.read(), cv2.IMREAD_COLOR)

    # Implement image preprocessing according to your requirements
    # For example, resize the image to the desired width and height
    width = 224  # Desired width
    height = 224  # Desired height
    resized_img = cv2.resize(img, (width, height))

    # Perform any additional preprocessing steps if required
    # ...

    return resized_img

def find_best_match(uploaded_image):
    
    dataset_path = 'path_to_your_dataset_folder'  # Specify the path of your dataset folder
    dataset_images = os.listdir(dataset_path)

    # Implement your image comparison algorithm to find the best match
    best_match_filename = ""

    # ...

    return best_match_filename

def match_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']

        # Save the uploaded image temporarily
        image_path = default_storage.save('temp/' + uploaded_image.name, uploaded_image)
        image_full_path = os.path.join(settings.MEDIA_ROOT, image_path)

        # Preprocess the uploaded image
        processed_image = preprocess_image(image_full_path)

        # Compare the uploaded image with the dataset images
        best_match_filename = find_best_match(processed_image)

        # Render the result or return the best match filename
        if best_match_filename:
            context = {
                'uploaded_image': uploaded_image,
                'best_match_filename': best_match_filename,
            }
            return render(request, 'result.html', context)
        else:
            return JsonResponse({'error': 'No match found'})

    return render(request, 'upload.html')

def crop_disease_list(request):
    crop_diseases = CropDisease.objects.all()
    data = []

    for crop_disease in crop_diseases:
        data.append({
            'crop': crop_disease.crop.name,
            'disease': crop_disease.disease.name,
            'description': crop_disease.description,
            'image': crop_disease.image.url if crop_disease.image else None,
        })

    return JsonResponse(data, safe=False)



@csrf_exempt
def bot(request): 
    prompt = request.POST["Body"]
    # sender_name = request.POST['ProfileName']
    # message = ''
    print(prompt)

    if prompt == 'hi':
     message= client.messages.create(
           from_='whatsapp:+14155238886',
           body='Welcome to Murimi bot please select the region you are coming',
           to='whatsapp:+263713872372'
        )
    # print(message.sid)
    return HttpResponse("hello")
   