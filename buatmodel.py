import numpy as np


def buatmodel(data):
    nlayer = len(data)
    rho = [_[1] for _ in data]
    ketebalan = [float(_[2]) for _ in data[:-1]]

    

    n_layer = len(rho)
    kedalaman = [0]

    dummy_rhop = [rho, rho]
    dummy_rhop = np.reshape(dummy_rhop, int(n_layer*2), order='F')
    rho = dummy_rhop
    rhop = rho


    #hitung kedalaman
    for i in range(1, n_layer):
        kedalaman.append(kedalaman[i-1] + ketebalan[i-1])

    kedalaman = [kedalaman, kedalaman]
    kedalaman = np.reshape(kedalaman, int((n_layer)*2), order='F')
    kedalaman = [kedalaman[_] for _ in range(1,int(n_layer*2))]
    kedalaman.append(99999999999)

    
    return rhop, kedalaman



# if __name__ == '__main__':
#     data, fdata = ambilmodel('..\Model 5 lapisan tanah.txt')   
#     #print(data)
#     #print(fdata) 
#     rhop, kedalaman = buatmodel(data)
#     print(rhop)
#     print(kedalaman)