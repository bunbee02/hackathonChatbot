from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from sklearn.cluster import KMeans
import cv2
import json
import numpy as np
import csv
import os
from PIL import Image
from . import datasets
from django.conf import settings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Create your views here.
from rest_framework import generics
from .models import Product, info, CropDisease
from .serializers import ProductSerializer, InfoSerializer




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




# def info_list(request):
#     # Fetch data from the info table
#     info_queryset = info.objects.all()

#     # Prepare combined data
#     combined_data = []

#     # Add data from the info table
#     for information in info_queryset:
#         combined_data.append({
#             'label': information.label,
#             'humidity': float(information.humidity),
#             'ph': float(information.ph),
#             'rainfall': float(information.rainfall),
#             'temperature': float(information.temperature),
#         })

#     # Get the path to the CSV file
#     csv_file_path = os.path.join(os.path.dirname(__file__), 'info.csv')

#     # Read data from the CSV file
#     with open(csv_file_path, 'r') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             combined_data.append({
#                 'label': row['label'],
#                 'humidity': float(row['humidity']),
#                 'ph': float(row['ph']),
#                 'rainfall': float(row['rainfall']),
#                 'temperature': float(row['temperature']),
#             })

#     # Perform clustering
#     data = np.array([
#         [d['humidity'], d['ph'], d['rainfall'], d['temperature']]
#         for d in combined_data
#     ])
#     kmeans = KMeans(n_clusters=3)
#     kmeans.fit(data)

#     # Get the cluster labels assigned by the algorithm
#     cluster_labels = kmeans.labels_.tolist()  # Convert to list

#     # Assign labels to the clusters
#     cluster_names = {
#         0: "Wheat",
#         1: "Rice",
#         2: "Corn"
#     }

#     # Prepare the data with assigned cluster labels and names
#     clustered_data = []
#     for i, label in enumerate(cluster_labels):
#         d = combined_data[i]
#         d['cluster_label'] = label
#         d['cluster_name'] = cluster_names[label]
#         clustered_data.append(d)

#     return JsonResponse(clustered_data, safe=False)

def train_model(data):
    # Prepare the data for training
    X = np.array([[d['humidity'], d['ph'], d['rainfall'], d['temperature']] for d in data])

    # Perform K-means clustering
    k = 3  # Number of clusters
    if len(X) >= k:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(X)

        # Get the cluster labels
        labels = kmeans.labels_

        # Add the cluster labels to the data
        for i, d in enumerate(data):
            d['cluster'] = int(labels[i])  # Convert to regular integer
    else:
        raise ValueError('Insufficient data samples for clustering')

    return data


def evaluate_model(X, y):
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    trained_model = train_model(X_train)

    # Evaluate the model on the test set
    y_pred = [d['cluster'] for d in trained_model]
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy





def info_list(request):
    # Fetch data from the info table
    info_queryset = info.objects.all()

    # Serialize the data from the Django table
    serializer = InfoSerializer(info_queryset, many=True)
    serialized_data = serializer.data

    # Prepare the data for clustering
    data = []
    for item in serialized_data:
        data.append([item['temperature'], item['humidity'], item['ph'], item['rainfall']])

    # Get the path to the CSV file
    csv_file_path = os.path.join(os.path.dirname(__file__), 'info.csv')

    # Read data from the CSV file
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append([float(row['temperature']), float(row['humidity']), float(row['ph']), float(row['rainfall'])])

    # Perform K-means clustering
    k = 3  # Number of clusters
    if len(data) >= k:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data)

        # Get the cluster labels
        labels = kmeans.labels_

        # Convert cluster labels to regular Python integers
        labels = [int(label) for label in labels]

        # Add the cluster labels to the serialized data
        for i, item in enumerate(serialized_data):
            item['cluster'] = labels[i]
    else:
        return JsonResponse({'error': 'Insufficient data samples for clustering'})

    return JsonResponse(serialized_data, safe=False)




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