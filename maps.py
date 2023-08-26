import requests
import urllib

#CONEXION PARA API
api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "TAnOJShf5zfrlA5UwDZevavrsqT3VlNw"

#BUCLE REPETITIVO PARA CARGA DE DATOS
while True:
    origin = input("Ingresa el origen: ")
    if origin == "x":
        break
    destination = input("Ingresa el destino: ")
    if destination == "x":
        break

    #TOMA DE DATOS DE LA API
    url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"]*1.61
        #fuel_used = json_data["route"]["fuelUsed"]*3.78
        print("INFO".center(50,"-"))
        print(f'Informacion del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.')
        print("TIEMPO ESTIMADO".center(50,"-"))
        print(trip_duration)
        print(f'{round(distance,2)} KM.')
        print("COMBUSTIBLE UTILIZADO".center(50,"-"))
        #print(f'{round(fuel_used,2)} LTS.')
        print(url)


#IMPRESION DE INDICACIONES Y DISTANCIA FALTANTE
        for each in json_data["route"]['legs'][0]['maneuvers']:
            distance_remaining= distance - each["distance"] * 1.61
            print(each["narrative"]+" ("+str(round(distance_remaining))+ " KMs)")
            distance= distance_remaining