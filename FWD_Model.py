import numpy as np
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tabulate import tabulate
import art
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# IMPORT FUNGSI YANG LAIN
from ambilmodel import ambilmodel
from buatmodel import buatmodel
from plotforward import plotforward



def main():
    con = True
    print('================================')
    art.tprint('FORWARD \n MODELLING')
    while con:
        print('================================')
        print('MENU FORWARD MODELLING')
        print('Opsi:')
        print('\t1. Open File')
        print('\t2. Save Data')
        print('\t3. Proses data')
        print('\t4. Lihat Plot')
        print('\t5. Properti Model')
        print('================================')
        opsi = int(input('Masukan pilihan yang diinginkan (keluar: 0): '))

        if opsi == 0: #keluar
            print('Keluar dari program...')
            con = False 


        elif opsi == 1: # open file

            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
            try:
                print('Loading model...')
                data, fdata = ambilmodel(filename)
                # print(f'data = {data}')
                # print(f'fdata = {fdata}')
                print('STATUS: Model sudah dimasukkan.')

            except:
                pass
            

        elif opsi == 2: # Save File
            Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
            ftypes = [('Text document', '.txt')]
            savefilename = asksaveasfilename(defaultextension=".txt", filetypes=ftypes, title='Save Data Hasil')
            print(savefilename)


            try:

                writedata = [f'{_[0]:.6f}\t{_[1]:.6f}\t{_[2]:.6f}\n' for _ in np.transpose([fdata.frekuensi, rhoapp, fasa])]
                
                print(writedata)
                with open(savefilename, 'w') as f:
                    f.write('frekuensi\t Apparent Resistivity\t Fasa\n')
                    for wd in writedata:
                        
                        f.write(wd)
                    
                    pass

                pass




            except:
                print('Error: Failed to save data')

            pass


        elif opsi == 3: # Proses Data
            
            try:
                rhop, kedalaman = buatmodel(data)
                rhop = [float(_) for _ in rhop]
                kedalaman = [float(_) for _ in kedalaman]
            except:
                print('ERROR: DATA BELUM ADA!')

            try:
                rhoapp, fasa, saturasi = plotforward(data, fdata, kedalaman, rhop)
                #print(f'rhoapp = {rhoapp}')
                #print(f'fasa = {fasa}')
            except:
                print('ERROR: PLOTFORWARD')
                

        elif opsi == 4: # PLOT DATA
            
            fig = plt.figure(constrained_layout=True)
            gs = fig.add_gridspec(2,2)
            ax1 = fig.add_subplot(gs[0,0])
            ax2 = fig.add_subplot(gs[1,0])
            ax3 = fig.add_subplot(gs[:,1])
            #ax4 = fig.add_subplot(gs[:,2])


            ax1.plot(fdata.frekuensi, rhoapp, 'r-', linewidth=3)
            ax1.set_yscale('log')
            ax1.set_xscale('log')
            ax1.set_title('Apparent Resistivity')
            ax1.set_xlabel('frekuensi (Hz)')
            ax1.set_ylabel(r'$\rho_a$ ($\Omega$m)')
            ax1.grid(True)
            ax1.invert_xaxis()
            ax1.set_xlim(min(fdata.frekuensi)/2, max(fdata.frekuensi))
            ax1.set_ylim(min(rhoapp)/5, max(rhoapp)*5)
            

            ax2.plot(fdata.frekuensi, fasa, 'r-', linewidth=3)
            #ax2.set_yscale('log')
            ax2.plot(fdata.frekuensi, np.ones(len(fdata.frekuensi))*45, 'k--', linewidth=5)
            ax2.set_xscale('log')
            ax2.set_title('Fasa')
            ax2.set_xlabel('frekuensi (Hz)')
            ax2.set_ylabel(r'$\phi$ ($\circ$)')
            ax2.set_xlim(min(fdata.frekuensi)/2, max(fdata.frekuensi))
            ax2.set_ylim(0, 90)
            ax2.invert_xaxis()
            ax2.grid(True)


            ax3.plot(rhop, kedalaman, 'r-', linewidth=3)
            ax3.set_xscale('log')
            ax3.set_ylabel('Kedalaman (m)')
            ax3.set_xlabel(r'Resistivity ($\Omega$m)')
            ax3.set_xlim(min(rhop)/5, max(rhop)*5)
            if len(kedalaman)>2:
                ax3.set_ylim(0, max([abs(_) for _ in kedalaman[:-1]])*1.2)
            ax3.invert_yaxis()
            ax3.grid(True)
            ax3.set_title('Respon Resistivitas')


            # ax4.plot(saturasi, kedalaman, 'r-', linewidth=3)
            # ax4.set_xscale('log')
            # ax4.set_ylabel('Kedalaman (m)')
            # ax4.set_xlabel('Saturasi')
            # ax4.set_xlim(min(saturasi)/5, max(saturasi)*5)
            # if len(kedalaman)>2:
            #     ax4.set_ylim(0, max([abs(_) for _ in kedalaman[:-1]])*1.2)
            # ax4.invert_yaxis()
            # ax4.grid(True)


            plt.tight_layout()
            plt.show(block=False)
            


        elif opsi == 5: #properti model
            
            try:
                print('MODEL PROPERTI')
                print(f'Rentang Frekuensi: {min(fdata.frekuensi)} - {max(fdata.frekuensi)}')

                modelprop = data
                modelprop[-1][2] = 'homogeneus halfspace'
                print(tabulate(modelprop, headers=['No', 'Resistivity', 'Ketebalan']))

            except:
                print('ERROR: Model Properti')

                pass
                



if __name__ == '__main__':
    main()