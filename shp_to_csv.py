""" Convert OSM produced shapefiles into list of schools, hospitals etc with lat/longs

Sara Terp
2015
"""

import fiona
from shapely.geometry import shape
import csv

def cleantext(intext):
	if intext == None:
		return("")
	else:
		return(intext.encode('utf-8'))


src = fiona.open("medical_polygon.shp/medical_polygon.shp", "r")
fout = open("medical_polygon.csv", "wb")
csvout = csv.writer(fout, quoting=csv.QUOTE_NONNUMERIC)  

#Create headers
headers = ['amenity', 'name', 'latitude', 'longitude', 'ogc id', 'OSM way id'];
csvout.writerow(headers)

#Write features to file
for f in src:
	props = f['properties']

	gbounds = shape(f['geometry']).bounds  #Lon then lat
	lon = (gbounds[0]+gbounds[2])/2.0;
	lat = (gbounds[1]+gbounds[3])/2.0;

	outrow = []
	outrow += [cleantext(props['AMENITY'])]
	outrow += [cleantext(props['NAME'])]
	outrow += [lat]
	outrow += [lon]
	outrow += [props['OGC_FID']]
	outrow += [cleantext(props['OSM_WAY_ID'])]
	#outrow += [props['OTHER_TAGS']].encode('utf-8')
	print("{}".format(outrow))
	csvout.writerow(outrow)

fout.close()