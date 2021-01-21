import numpy as np

class frekuensidata:
    def __init__(self, fmin, fmax, bagi, frekuensi):
        self.fmin = fmin;
        self.fmax = fmax;
        self.bagi = bagi;
        self.frekuensi = frekuensi;


def ambilmodel(model):
    with open(model,'r') as reader:
        #ambil data
        pick = reader.readlines()

    freq = pick[0].split()
    fmin = float(freq[1]) 
    fmax = float(freq[2])
    bagi = int(freq[3])
    #print(fmin)
    rentang = [np.log10(fmin),  np.log10(fmax)]

    xf = [1, bagi]
    x = list(range(1,31))
    log_frekuensi = np.interp(x, xf, rentang) # rentang log frekuensi
    #print(log_frekuensi)

    frekuensi = [10**_ for _ in log_frekuensi]
    #print(frekuensi)

    fdata = frekuensidata(fmin, fmax, bagi, frekuensi)
    
    header = pick[1].split()
    #print(pick[1].split())

    a = [_ for _ in pick[2:] ]
    #print(a)
    
    for b in a:
        c = b.split()
        try:
            [float(_) for _ in c]
        except:
            break
        if not c:
            break

        try:
            data = np.vstack((data,c))
        except:
            data = c
            


    #print(data)
    return data, fdata





# if __name__ == '__main__':
#     data, fdata = ambilmodel('Model 4 lapisan tanah.txt')   
#     print(data)
#     print(fdata) 