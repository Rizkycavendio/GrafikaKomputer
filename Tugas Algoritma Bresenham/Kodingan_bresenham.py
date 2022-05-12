# -*- coding: utf-8 -*-

#MUHAMMAD RIZKY CAVENDIO - 20051397011 Kelas A

import matplotlib.pyplot as plt
import numpy as np

#VERTEX AWAL
x1= 1;
y1= 9;
x2= 3;
y2= 7;

#RUMUS MENCARI NILAI DARI DELTA X DAN Y
dx = x2- x1
dy = y2- y1

#RUMUS UNTUK MENDAPATKAN NILAI GRADIEN M
m = dy/dx;

#UNTUK MENGHITUNG PARAMETERNYA
p=(2*abs(dx))-abs(dy);

#TEMPAT MENAMPUNG VERTEX/TITIK
tamp=[];tamp2=[];

#MENDEFINISIKAN X DAN Y
X = x1;
Y = y1;

#Masukkan x dan y ke dalam list
tamp.append(X);
tamp2.append(Y);

#LOGIC LOOPING
for x in range(99999):
    #JIKA NILAI P < 0
    if p < 0:
        X = X;
        Y = Y+1;
        p = p + (2*abs(dx));
     #JIKA NILAI P > 0
    else:
        X = X+1;
        Y = Y+1;
        p = p + (2*abs(dx))-(2*abs(dy))
        
    #NANTI DITAMPUNG DI DALAM SINI
    tamp.append(X);
    tamp2.append(Y);
    
    #UNTUK MENENTUKAN POSISI PIKSEL SAMPAI BERHENT
    if X==x1 and Y==y1:
        break;

#MENGUBAH TAMPILAN MENJADI ARRAY
xpoints = np.array(tamp)
ypoints = np.array(tamp2)

#MENAMPILKAN HASILNYA 
plt.plot(xpoints, ypoints, '-')
plt.show()