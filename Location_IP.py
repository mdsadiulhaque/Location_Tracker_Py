import geocoder
ip = geocoder.ip("161.185.160.93")
#ip = geocoder.ip('me')
print(ip.city)
print(ip.latlng)
location = ip.latlng
import folium
location = ip.latlng

map = folium.Map(location=location, zoom_start=10)
folium.CircleMarker(location=location, radius=50, color="red").add_to(map)
folium.Marker(location).add_to(map)

map

map.save("map.html")

print(map.save)