#!/usr/bin/env python3
import sys
import numpy as np
import math
import statistics as stat


#function to separate the ra, dec and cz from the rest of the file 
def readgalaxy (filename):
    try:
        ra, dec, cz = np.genfromtxt(filename, unpack = True, usecols = (0,1,4),dtype = float, delimiter = ',')
    except FileNotFoundError:
        print("filename invalid")

    return ra[1:], dec[1:], cz[1:] 

def main():
    i = 0 #loop counter
    valid_gals = []

    galaxyfile = sys.argv[1]
    key = sys.argv[2] #filter which cluster we are looking at
    
    ra, dec, cz = readgalaxy(galaxyfile)

    with open(galaxyfile, "r") as galf:
        lines = galf.readlines()
        if key == 'abell':
            for i in range(len(lines)-1):
                dist = math.sqrt((ra[i]-258.1292)**2 + (dec[i]-64.0925)**2)
                if (dist <= 5 and (cz[i] >= 18000 and cz[i] <=30000)):
                    valid_gals.append(lines[i])
                
            with open("filtered_a.csv", "w") as newfile:
                for j in range(len(valid_gals)):
                    newfile.write(valid_gals[j])

        if key  == 'coma':
            for i in range(len(lines)-1):
                dist = math.sqrt((ra[i]-194.95799)**2 + (dec[i]-27.98300)**2)
                if (dist <= 5 and (cz[i] >= 4500 and cz[i] <= 9250)):
                    valid_gals.append(lines[i])
                
            with open("filtered_c.csv", "w") as newfile:
                for k in range(len(valid_gals)):
                    newfile.write(valid_gals[k])        

    return




if __name__ == "__main__":
    main()
