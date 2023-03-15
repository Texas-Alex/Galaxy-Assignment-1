#!/usr/bin/env python3
import sys
import numpy as np
import math
import statistics as stat

def readgalaxy (filename):
    try:
        ra, dec, cz = np.genfromtxt(filename, unpack = True, usecols = (0,1,4), dtype = float, delimiter = ',')
    except FileNotFoundError:
        print("filename invalid")

    return ra, dec, cz


def projected_radius(ra_g, dec_g, ra_c, dec_c, N, dist):
    rad = 0.0
    for i in range(N):
        if math.sqrt((ra_g[i]-ra_c)**2 + (dec_g[i]-dec_c)**2)/dist > 0.1 : #verify small angle approximation             
            print("small angle approximation dies not hold!")

        rad += math.sqrt((ra_g[i]-ra_c)**2 + (dec_g[i]-dec_c)**2)*dist


    return rad/N

def harmonic_radius(ra, dec, N, dist):
    sum = 0.0
    for i in range(N):
        for j in range(N):
            if ra[i] != ra[j] and dec[i] != dec[j]: #verify its not the same galaxy
                if math.sqrt((ra[i]-ra[j])**2 + (dec[i]-dec[j])**2)/dist > 0.1: #verify small angle approximation
                    print("small angle approximation doesnt hold!")
                if i < j:
                    sum += 1/(math.sqrt((ra[i]-ra[j])**2 + (dec[i]-dec[j])**2)*dist)

    radius = (math.pi/2) * (N**2/sum)

    return radius

def main():
    filename = sys.argv[1]
    key = sys.argv[2]
    Hubble = 67.77

    ra, dec, cz = readgalaxy(filename)
    dist = stat.mean(cz)/Hubble
    print("mean cz for cluster " +key + " is: " + str(stat.mean(cz)))
    print("the distance to " + key + " cluster is: " + str(dist) + "Mpc")


    if key == 'abell':
        proj_radius =  projected_radius(ra,dec,258.1292,64.0925,len(ra), dist)
        print("projected radius is: " + str(proj_radius) +" Mpc")
        harm_radius = harmonic_radius(ra,dec,len(ra),dist)
        print("harmonic radius is: " + str(harm_radius) + " Mpc")

        return
    if key == 'coma':
        proj_radius =  projected_radius(ra,dec,194.95799,27.98300,len(ra),dist)
        print("projected radius is: " + str(proj_radius) + " Mpc")
        harm_radius = harmonic_radius(ra,dec,len(ra),dist)
        print("harmonic radius is: " + str(harm_radius) + " Mpc")
        return
    else:
        print("invalid key")
        return ValueError

    return

if __name__ == "__main__":
    main()