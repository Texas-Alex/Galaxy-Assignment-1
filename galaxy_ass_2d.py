#!/usr/bin/env python3
import sys
import numpy as np
import math
import statistics as stats

def readgalaxy (filename):
    try:
        ra, dec, cz = np.genfromtxt(filename, unpack = True, usecols = (0,1,4), dtype = float, delimiter = ',')
    except FileNotFoundError:
        print("filename invalid")

    return ra, dec, cz

def mass_vir(ra, dec, cz, cz_mean, N, dist):
   Vsum = 0.0
   rsum = 0.0
   G =  4.3*10**(-9) #pcM^-1 kms^-2
   for i in range(N):
      Vsum += (cz[i]-cz_mean)**2
      for j in range(N):
          if ra[i] != ra[j] and dec[i] != dec[j]: #verify its not the same galaxy
                if math.sqrt((ra[i]-ra[j])**2 + (dec[i]-dec[j])**2)/dist > 0.1: #verify small angle approximation
                    print("small angle approximation doesnt hold!")
                if i < j:
                    rsum += 1/(math.sqrt((ra[i]-ra[j])**2 + (dec[i]-dec[j])**2)*dist)

 
   
   M_vir = ((3*math.pi)/(2*G))*N*(Vsum/rsum)
   return M_vir



def main ():
    filename = sys.argv[1]
    key = sys.argv[2]
    Hubble = 67.77

    ra, dec, cz = readgalaxy(filename)
    dist = stats.mean(cz)/Hubble
    cz_mean = stats.mean(cz)
    


    mass = mass_vir(ra,dec, cz,cz_mean, len(ra), dist)
    print("the mass of " + key + " cluster is: " + str(mass) + " solar masses")
    
    
    
    return


if __name__ == "__main__":
    main()