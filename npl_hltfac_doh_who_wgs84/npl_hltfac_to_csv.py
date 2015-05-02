""" Convert WorldBank produced shapefiles into list of schools, hospitals etc with lat/longs

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


src = fiona.open("npl_hltfac_DoH_WHO_wgs84.shp", "r")
fout = open("npl_hltfac_DoH_WHO_wgs84.csv", "wb")
csvout = csv.writer(fout, quoting=csv.QUOTE_NONNUMERIC)  

#Create headers
headers = ['hf_type', 'dist_name', 'vdc_name1', 'vdc_code1','latitude', 'longitude'];
csvout.writerow(headers)

#Write features to file
for f in src:
	props = f['properties']

	gbounds = shape(f['geometry']).bounds  #Lon then lat
	lon = (gbounds[0]+gbounds[2])/2.0;
	lat = (gbounds[1]+gbounds[3])/2.0;

	outrow = []
	outrow += [cleantext(props['HF_TYPE'])]
	outrow += [cleantext(props['DIST_NAME'])]
	outrow += [cleantext(props['VDC_NAME1'])]
	outrow += [cleantext(props['VDC_CODE1'])]
	outrow += [lat]
	outrow += [lon]
	#outrow += [props['OTHER_TAGS']].encode('utf-8')
	print("{}".format(outrow))
	csvout.writerow(outrow)

fout.close()