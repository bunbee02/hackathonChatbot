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







class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    



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
    resp = {}

    if prompt == 'hi':
        message= client.messages.create(
        from_='whatsapp:+14155238886',
        body='''Welcome to Murimi bot please select the region you are coming
        1. Mashonaland Central
        2. Mashonaland East
        3. Mashonaland West
        4. Matebeleland North
        5. Matebeleland South
        6. Harare
        7. Manicaland
        8. Midlands
        9. Masvingo
        10. Bulawayo. 
        ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '1':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Mashonaland Central and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            soyabeans
            groundnuts
            cabbages''',
        to='whatsapp:+263713872372'
        )

    if prompt == '2':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Mashonaland East and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            wheat
            cabbages''',
        to='whatsapp:+263713872372'
        )

    if prompt == '3':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Mashonaland West and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )

    if prompt == '7':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Manicaland and in this province these are the crops that you can plant
            maize
            tea
            cotton
            soya beans
            sunflower
            wheat
            ''',
        to='whatsapp:+263713872372'
        )

    if prompt == '8':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Midlands and in this province these are the crops that you can plant
            maize
            wheat
            soyabeans
            sunflower
            cotton
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '3':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Mashonaland West and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '9':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Masvingo and in this province these are the crops that you can plant
            maize
            sugarcane
            cotton
            citrus fruits
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '4':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Matebeleland North West and in this province these are the crops that you can plant
            maize
            sorghum
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '6':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Harare and in this province these are the crops that you can plant
            maize
            wheat
            potatoes
            vegetables
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == '5':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Matebeleland South and in this province these are the crops that you can plant
            maize
            sorghum
            wheat
            cotton
            sunflower
            ''',
        to='whatsapp:+263713872372'
        )

    if prompt == '10':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == 'maize':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Maize
                Choose the right variety: Select a maize variety that is well-suited for your climate, soil type, and intended use (e.g., sweet corn, field corn, or popcorn). Consider factors such as disease resistance, yield potential, and maturity length.

                Prepare the soil: Maize thrives in well-drained, fertile soil. Start by clearing the area of weeds and debris. Loosen the soil using a garden fork or tiller. Incorporate organic matter, such as compost or well-rotted manure, to improve soil fertility and structure.

                Plan the planting time: Maize is a warm-season crop and requires soil temperatures of at least 50°F (10°C) for germination. The exact planting time will depend on your location and climate. In general, plant maize after the last frost date in your area and when the soil has warmed up.

                Sow the seeds:

                Dig furrows or trenches in the prepared soil, spaced about 2-3 feet apart, to allow for proper plant spacing and airflow.
                Plant the maize seeds at a depth of about 1-2 inches, placing them 6-12 inches apart within the row.
                Cover the seeds with soil and gently firm it down.
                                
                These dressings break down after 21 days so there can be a risk where there is slow emergence of seed in cold, wet seed-beds.
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == 'tobacco':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Tobbaco
           Legal Considerations:

        Research and comply with the legal requirements and regulations for tobacco cultivation in your region. Obtain any necessary permits or licenses.
        Familiarize yourself with any specific restrictions or regulations related to selling, processing, or manufacturing tobacco.
        Choose the Right Variety:

        Select a tobacco variety suitable for your climate and soil conditions. Different tobacco types include flue-cured, burley, oriental, and cigar wrapper tobacco. Each type has specific requirements and characteristics.
        Soil Preparation:

        Tobacco requires well-drained, fertile soil. Conduct a soil test to assess the nutrient composition and pH levels of your soil.
        Prepare the soil by removing weeds and debris. Till the soil to a depth of around 6-8 inches, incorporating organic matter such as compost or well-rotted manure.
        Adjust the soil pH to the recommended range for your chosen tobacco variety.
        Seedbed Preparation:
                    ''',
        to='whatsapp:+263713872372'
        )
    if prompt == 'cotton':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            limate and Soil:

        Cotton requires a warm climate, with temperatures ranging between 60°F (15°C) and 95°F (35°C) during the growing season.
        Choose a location with well-drained soil. Cotton thrives in loamy or sandy soil with good moisture retention. The soil should have a pH between 5.8 and 7.0.
        Variety Selection:

        Select cotton varieties that are suitable for your region and climate. Consider factors such as disease resistance, yield potential, fiber quality, and maturity length.
        Consult local agricultural extension services or seed suppliers for recommendations on suitable cotton varieties.
                    ''',
        to='whatsapp:+263713872372'
        )
    if prompt == 'soyabeans':
              message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
              
    if prompt == 'groundnuts':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )
    if prompt == 'wheat':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )

    if prompt == 'sunflower':
        message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=''' You selected Bulawayo and in this province these are the crops that you can plant
            maize
            tobbacco
            cotton
            sugarcane
            groundnuts
            ''',
        to='whatsapp:+263713872372'
        )

        return HttpResponse("hello")
        
    # elif prompt.lower == "mashonaland":
    #     message = client.messages.create(
    #     from_='whatsapp:+14155238886',
    #     body='You selected mashonalad',
    #     to='whatsapp:+263713872372'
    #     )
    #     return HttpResponse("hello")


    

        # print(message.sid)
    else: 
        print('did not work')
        return HttpResponse('No file')

   