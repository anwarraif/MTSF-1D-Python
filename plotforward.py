import numpy as np
import matplotlib.pyplot as plt

from ForwardModel import ForwardModel

#testing


def hitung(data, fdata):

    nlayer = int(len(data))
    rho = [float(_[1]) for _ in data]
    ketebalan = [float(data[i][2]) for i in range(nlayer-1)]
    frekuensi = fdata.frekuensi

    rhoapp = np.zeros(len(frekuensi))
    fasa = np.zeros(len(frekuensi))
    for i in range(len(frekuensi)):
        rhoapp[i], fasa[i] = ForwardModel(rho, ketebalan, frekuensi[i])

    saturasi = [ 1/rho[i]**0.5 for i in range(len(rho)) ]

    dummy_sat = [saturasi, saturasi]
    dummy_sat = np.reshape(dummy_sat, int(len(rho)*2), order='F')
    saturasi = dummy_sat

    return rhoapp, fasa, saturasi



def plotforward(data, fdata, kedalaman, rhop):

    frekuensi = fdata.frekuensi

    rhoapp, fasa, saturasi = hitung(data, fdata);

    return rhoapp, fasa, saturasi



if __name__ == '__main__':
    
    from ambilmodel import ambilmodel
    from buatmodel import buatmodel

    data, fdata = ambilmodel('../Model 5 lapisan tanah.txt')
    print(f'data = {data}')
    print(f'fdata = {fdata}')

    try:
        rhop, kedalaman = buatmodel(data)
    except:
        print('ERROR: DATA BELUM ADA!')

    rhoapp, fasa, saturasi = plotforward(data, fdata, kedalaman,rhop)
    print(f'rhoapp = {rhoapp}')
    print(f'fasa = {fasa}')

