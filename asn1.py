# NAME: fantuo meng
# ST-NUMBER: 250919681
# WORKED WITH: my mac
import math

def load_asn1_data():

	import csv
	
	reader = csv.reader(open('starbucks.csv', 'r'))
	locations = []
	
	for r in reader:
		locations.append( (r[0],r[1]))
		
	return locations
	
	
def convert_to_decimal(degrees,minutes,seconds):
    b=minutes/float(60)
    c=seconds/float(3600)
    return float(degrees+b+c)
    pass
	

def subtended_area(lat1,lon1,lat2,lon2):

    i=math.sin(lat1)-math.sin(lat2)
    u=abs(i)
    j=abs(lon1-lon2)
    r=6378.1
    
    return r*r*u*j*(math.pi)/180
	

def num_starbucks(locations,lat1,lon1,lat2,lon2):
        	
    count=0
    for loc in locations:
        loc_lat = float(loc[1])
        loc_lon = float(loc[0])
				
		#print loc_lat, loc_lon,  (lat1 < loc_lat), ( loc_lat < lat2), (lon1 < loc_lon), (loc_lon < lon2)
		# Okay, loc_lat now contains the latitude of the location we're considering.
		# Likewise, loc_lon contains the longitude. What _you_ have to do is:
		# - figure out if loc_lat lies between lat1 and lat2 AND loc_long lies between lon1 and lon2
		# - if that's the case, increment a variable containing the number of starbucks
		# - otherwise... do nothing at all
		
		
		# INSERT YOUR CODE HERE!
        if(loc_lat < lat2) and (loc_lon < lon2) and (loc_lon > lon1) and (loc_lat > lat1):
       
        #if(lat1<loc_lat<lat2) and (lon1<loc_lon<lon2):           
            count=count+1
    return count
	# RETURN the value in your counter variable
	
def starbucks_per_kmsq(lat1, lon1, lat2, lon2):
	# INSERT YOUR CODE HERE!
    g=load_asn1_data()
    area=subtended_area(lat1,lon1,lat2,lon2)
    n=num_starbucks(g,lat1,lon1,lat2,lon2)
    density=n/area
    return density