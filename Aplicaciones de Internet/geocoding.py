#Prueba geocoder
import geocoder
g = geocoder.osm('ESCOM, MX')
print(g.ok)
print(g.geojson)
print(g.json)
print (g.wkt)
print (g.osm)