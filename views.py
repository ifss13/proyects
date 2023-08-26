from django.shortcuts import render
import requests
import urllib

#CONEXION PARA API
api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "TAnOJShf5zfrlA5UwDZevavrsqT3VlNw"

# Create your views here.
def home(request):
    return render(request,"index.html")

def procesar(request):
    if request.method == 'POST':
        mi_textbox = request.POST['mi_textbox']
        mi_textbox2 = request.POST['mi_textbox2']
        url = api_url + urllib.parse.urlencode({"key":key,"from":mi_textbox,"to":mi_textbox2})
        json_data = requests.get(url).json()
        status_code = json_data["info"]["statuscode"]
        if status_code == 0:
            trip_duration = json_data["route"]["formattedTime"]
            distance = json_data["route"]["distance"]*1.61
            distance = round(distance,2)
        return render(request, 'resultado.html', {'mi_textbox': mi_textbox,'mi_textbox2': mi_textbox2,'duracion':trip_duration,'distancia':distance})
    return render(request, 'index.html')

#def calcular(mi_textbox,mi_textbox2):
    url = api_url + urllib.parse.urlencode({"key":key,"from":mi_textbox,"to":mi_textbox2})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"]*1.61
