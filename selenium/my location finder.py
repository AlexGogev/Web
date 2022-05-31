import geocoder
import requests




g = geocoder.ip('me')
full_address = g.latlng
lat = full_address[0]
lng = full_address[1]
print(g.country, g.street)


