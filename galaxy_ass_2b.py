#!/usr/bin/env python3
import sys
import numpy as np
import statistics as stat


#function to separate the ra, dec and cz from the rest of the file 
# the raw files used still contain a header that is removed when reading the file
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

    
    #read the file line by line and determine if it is close enough within the cluster
    #checks which cluster to ensure the right values are used for ra and dec along with writing the correctly named filtered_ file
    with open(galaxyfile, "r") as galf:
        lines = galf.readlines()
        
        if key == 'abell':
            for i in range(len(lines)-1):
                if (ra[i] >= 257.6 and ra[i]<= 258.6) and (dec[i] >= 63.5 and dec[i] <=64.5 )and (cz[i] >= 18000 and cz[i] <=30000):
                    valid_gals.append(lines[i])
                
            with open("filtered_a.csv", "w") as newfile:
                for j in range(len(valid_gals)):
                    newfile.write(valid_gals[j])

        if key  == 'coma':
            for i in range(len(lines)-1):
                if (ra[i] >= 194. and ra[i] <= 195.4) and (dec[i] >= 27.2 and dec[i] <= 28.3) and (cz[i] >= 4500 and cz[i] <= 9250):
                    valid_gals.append(lines[i])
                
            with open("filtered_c.csv", "w") as newfile:
                for k in range(len(valid_gals)):
                    newfile.write(valid_gals[k])        

    return




if __name__ == "__main__":
    main()
