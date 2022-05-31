import geocoder
import requests
import json



g = geocoder.ip('me')
full_name = g.latlng
lat = full_name[0]
lng = full_name[1]
url = f"https://data.police.uk/api/crimes-street/Burglary?lat={lat}&lng={lng}&date=2022-02"

#f"https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date=2017-01"
data = requests.get(url=url)
extracted = data.json()
print(extracted)
# with open("text.txt" ,  "w") as text:
#     text.write(extracted)
for i in extracted:
    location = i["location"]["street"]["name"]
    category = i["category"]
    status = i["outcome_status"]
    with open("text.txt", "a") as text:
        text.write(f"{category} -> {status} -> {location}   \n")

