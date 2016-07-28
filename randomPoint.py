#!/usr/bin/env python2

##########
#
#  I totally effing stole this from stack exchange.  
#  https://gis.stackexchange.com/questions/25877/how-to-generate-random-locations-nearby-my-location
#
##########


from __future__ import division
import numpy as np
from haversine import haversine as h_dist

def create_random_point(x0,y0,distance):
    """
            Utility method for simulation of the points
    """   
    r = distance/ 111300
    u = np.random.uniform(0,1)
    v = np.random.uniform(0,1)
    w = r * np.sqrt(u)
    t = 2 * np.pi * v
    x = w * np.cos(t)
    x1 = x / np.cos(y0)
    y = w * np.sin(t)
    return (x0+x1, y0 +y)



if (__name__ == "__main__"):
    lat1,long1 = 43.6187,-116.2146
    x,y = create_random_point(lat1, long1, 100000)
    dist = h_dist((lat1, long1), (x,y), miles=False)
    print "Starting from \"%f,%f\"" % (lat1, long1)
    print "Headed toward \"%f,%f\"" % (x,y)
    print "Distance is %2.3f km" % dist

