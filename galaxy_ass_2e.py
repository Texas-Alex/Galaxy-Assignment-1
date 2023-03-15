#!/usr/bin/env python3
import sys
import numpy as np
import math
import statistics as stats


def readgalaxy (filename):
    try:
        ra, cz,lum = np.genfromtxt(filename, unpack = True, usecols = (0,4,-1),dtype = float, delimiter = ',')
    except FileNotFoundError:
        print("filename invalid")

    return ra, cz , lum

def main():
    filename = sys.argv[1]
    key = sys.argv[2]


    ra, cz, lum = readgalaxy(filename)
    HUBBLE = 67.77
    max_lum = 0.0
    count = 0
    print(lum[0])

    if key == "coma":
        DISTANCE = 103.198 # in Mpc
        for i in range(len(ra)):
            if cz[i]/HUBBLE <=DISTANCE+1 and cz[i]/HUBBLE >= DISTANCE-1:
                count +=1
                if lum[i] >  max_lum:
                    max_lum = lum[i]
        S_mass = max_lum/3

        print("stellar mass of brightest galaxy in " + key + " cluster is "+ str(S_mass))


    if key == "abell":
        DISTANCE = 335.578 # in Mpc
        for i in range(len(ra)):
            if cz[i]/HUBBLE <=DISTANCE+1 and cz[i]/HUBBLE >= DISTANCE-1:
                count += 1
                if lum[i] >  max_lum:
                    max_lum = lum[i]
        S_mass = max_lum/3

        print("stellar mass of brightest galaxy in " + key + " cluster is " + str(S_mass))



    return


if __name__ == "__main__":
    main()