from django.views.generic import TemplateView
import os
from django.shortcuts import render
from config import settings
import csv
import requests
import uuid
from django.http import HttpResponse
from datetime import datetime
from .models import StarWarsData


class IndexView(TemplateView):
    template_name = 'base.html'


def list_csv_files(request):
    csv_folder_path = os.path.join(settings.MEDIA_ROOT, 'csv_files')  # Ustal pełną ścieżkę do folderu CSV
    csv_files = [f for f in os.listdir(csv_folder_path) if f.endswith('.csv')]
    context = {
        "data" : csv_files
    }
    return render(request, 'index.html', context)

def download_csv(request):
    response = requests.get('https://swapi.dev/api/people')
    data = response.json().get('results', [])
    unique_filename = f'{uuid.uuid4()}.csv'

    StarWarsData(filename=unique_filename, data=data).save()
    


    csv_folder_path = os.path.join(settings.MEDIA_ROOT, 'csv_files')
    csv_file_path = os.path.join(csv_folder_path, unique_filename)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for item in data:
            writer.writerow([item.get('name', ''), item.get('height', ''), item.get('mass', ''),
                            item.get('hair_color', ''), item.get('skin_color', ''), item.get('eye_color', ''),
                            item.get('birth_year', ''), item.get('gender', ''), parse_homeword(item.get('homeworld', '')),
                            datetime.now().strftime("%Y-%m-%d")
                            ])
    return HttpResponse(status=200)
        
def display_csv_content(request, file_name):
    csv_folder_path = os.path.join(settings.MEDIA_ROOT, 'csv_files')
    csv_file_path = os.path.join(csv_folder_path, file_name)

    with open(csv_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        csv_data = list(reader)

    context = {
        'file_name': file_name,
        'csv_data': csv_data,
    }
    return render(request, 'display_csv_content.html', context)

def parse_homeword(url):
    response = requests.get(url)
    data = response.json()
    return data.get("name", "")

def save_to_db(item):
    pass