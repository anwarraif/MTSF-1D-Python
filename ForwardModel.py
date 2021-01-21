import numpy as np 
import cmath
from numpy.lib.scimath import sqrt as csqrt

def ForwardModel(resistivities, thicknesses, frequency):




    MU = 4*np.pi*10**(-7) 

    w = 2*np.pi * frequency
    n = len(resistivities)
    
    impedances = np.zeros(n, dtype='complex_')
    # print('================================================================')
    
    # print(n)
    # print(resistivities)
    # print(thicknesses)

    # print('================================================================')
    impedances[n-1] = csqrt( csqrt(-1) * w * MU * float(resistivities[n-1]) )

    
    if n > 1: 
        for j in range(n-2,-1,-1):
            resistivity = float(resistivities[j])
            thickness = float(thicknesses[j])
            
            dj = csqrt(csqrt(-1) * (w * MU / resistivity ))
            wj = dj * resistivity

            ej = np.exp(-2 * thickness * dj)

            belowImpedance = impedances[j+1]
            rj = (wj - belowImpedance) / (wj + belowImpedance)
            re = rj * ej
            Zj = wj * ((1 - re) / (1 + re))
            impedances[j] = Zj

    Z = impedances[0] 
    absZ = abs(Z)
    apparentResistivity = absZ * absZ / (MU * w)
    phase = np.rad2deg( np.arctan2(np.imag(Z),  np.real(Z)) )



    return apparentResistivity, phase