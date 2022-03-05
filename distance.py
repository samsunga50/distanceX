#BingsMapAPIKey
key = ""

#Set Country
countryRegion = "Mauritius"

def distance(origin, destination):
    import json
    import requests

    url = "http://dev.virtualearth.net/REST/v1/Locations?countryRegion=" + countryRegion + "&addressLine=" + origin + "&maxResults=1&key=" + key

    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    response_dict = json.loads(response.text)
    origin_coordinates = str(response_dict['resourceSets'][0]['resources'][0]['point']['coordinates'])[1:-1]

    url = "http://dev.virtualearth.net/REST/v1/Locations?countryRegion=" + countryRegion + "&addressLine=" + destination + "&maxResults=1&key=" + key
    response = requests.request("GET", url, headers=headers, data=payload)

    response_dict = json.loads(response.text)
    destination_coordinates = str(response_dict['resourceSets'][0]['resources'][0]['point']['coordinates'])[1:-1]

    url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins=" + origin_coordinates + "&destinations=" + destination_coordinates + "&travelMode=driving&key=" + key
    response = requests.request("GET", url, headers=headers, data=payload)
    response_dict = json.loads(response.text)

    distance = str(response_dict['resourceSets'][0]['resources'][0]['results'][0]['travelDistance'])
    return distance


