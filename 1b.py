#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def f(M, M_s, a, phi_s):
   #plotting in terms of M ? 
    const = 0.4 * (M_s - M)
    first = (10**const)**(a+1)
    second =np.exp(-10**const)
    return ((phi_s*0.01)*first*second)


def main():
    #make a list of everything, add the colours to the plot
    phi_s = [1.8, 1.77,2.03,1.47,1.24,1.00,1.02,0.98,0.97,1.03,1.10]
    M_s = [-17.12+0.84,-17.54+0.84, -18.6+0.84,-20.09+0.84,-20.86+0.84,-21.3+0.84,-21.52+0.84,-21.63+0.84,-21.74+0.84,-21.99+0.84,-21.63+0.84]
    a = [-1.14,-1.17,-1.03,-1.1,-1.12,-1.17,-1.14,-1.12,-1.1,-1.07,-1.03]


    M = np.linspace(-24, -14)
    fig, ax = plt.subplots()
    plt.plot(M, np.log10(f(M,M_s[0],a[0],phi_s[0])), color='#301934', label = 'FUV') #FUV
    plt.plot(M, np.log10(f(M,M_s[1],a[1],phi_s[1])), color='#A020F0', label = 'NUV') #NUV
    plt.plot(M, np.log10(f(M,M_s[2],a[2],phi_s[2])), color='#0000FF', label = 'u') #u
    plt.plot(M, np.log10(f(M,M_s[3],a[3],phi_s[3])), color='#00FF00', label = 'g') #g
    plt.plot(M, np.log10(f(M,M_s[4],a[4],phi_s[4])), color='red', label = 'r') #r
    plt.plot(M, np.log10(f(M,M_s[5],a[5],phi_s[5])), color='#4B0082', label = 'i') #i
    plt.plot(M, np.log10(f(M,M_s[6],a[6],phi_s[6])), color='#FFA500', label = 'z') #z
    plt.plot(M, np.log10(f(M,M_s[7],a[7],phi_s[7])), color='#FFFF00', label = 'Y') #Y
    plt.plot(M, np.log10(f(M,M_s[8],a[8],phi_s[8])), color='#000000', label = 'J') #J
    plt.plot(M, np.log10(f(M,M_s[9],a[9],phi_s[9])), color='#ADD8E6', label = 'H') #H
    plt.plot(M, np.log10(f(M,M_s[10],a[10],phi_s[10])), color='#FF00FF', label = 'K') #K

    ax.set_ylim(-8,0)
    # ax.set_yscale('log')
    ax.set_xlabel('$M$')
    ax.set_ylabel('$\phi$ [mag$^{-1}$ Mpc$^{-3}]$')
    plt.legend()
    plt.show()
    # x = [1,2,3,4,5,6,7,8,9,10]
    # y = [14,19,3,6,7,3,9,12, 1, 11]


    # plt.plot(x,y)
    # plt.show()

if __name__ == "__main__":
    main()
