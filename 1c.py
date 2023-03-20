#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    phi_s = [1.8, 1.77,2.03,1.47,1.24,1.00,1.02,0.98,0.97,1.03,1.10]
    M_s = [-17.12+0.84,-17.54+0.84, -18.6+0.84,-20.09+0.84,-20.86+0.84,-21.3+0.84,-21.52+0.84,-21.63+0.84,-21.74+0.84,-21.99+0.84,-21.63+0.84]
    a = [-1.14,-1.17,-1.03,-1.1,-1.12,-1.17,-1.14,-1.12,-1.1,-1.07,-1.03]
    L_s = []
    rho = []
    lamb = [1535,2301,3557,4702,6175,7491,8946,10305,12354,16458,21603]
    c = 3e8 #ms-1


    for i in range(len(M_s)):
        flux = 10**(-((M_s[i]+48.6)/2.5))
        flux = flux * (c/(lamb[i]*10**-10))
        L_s.append(4*(math.pi)*((3.086e+19)**2)*flux) #erg s−1 
        rho.append((L_s[i])*(phi_s[i]*0.01*(0.6777**3))*math.gamma(a[i]+2))


    fig, ax = plt.subplots()
    plt.scatter(lamb,rho)
    ax.set_xlabel('Angstrom')
    ax.set_ylabel('$[erg/s/Mpc^3] $')
    ax.set_yscale('log')
    ax.set_xscale('log')
    
    plt.show()



    return


if __name__ == "__main__":
    main()