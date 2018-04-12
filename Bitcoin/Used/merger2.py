import numpy as np
import random
from pylab import *
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import math
import ast
import sys


#data1 = np.loadtxt("Bitcoin1/Data" + '1.csv', delimiter = ',')
#data2 = np.loadtxt("Bitcoin2/Data" + '2.csv', delimiter = ',')
#data3 = np.loadtxt("Bitcoin3/Pasado/Data" + '3.csv', delimiter = ',')
#data3p2 = np.loadtxt("Bitcoin3/Pasado/Data" + '3parte2.csv', delimiter = ',')
#data3 = data3.T
#data4 = np.loadtxt("Bitcoin4/Data" + '4.csv', delimiter = ',')

#ldat = len(data3[0])
#Tipos3 = np.loadtxt("Bitcoin3/Types3.csv", delimiter = ',')

arr1 = []
k = 0
Tipos2 = open ("Bitcoin2/Types2.csv","r")
for line in Tipos2.readlines():
	arr1.append([0 for x in range(6)])
	j = 0
	for i in ast.literal_eval(line):
		arr1[k][j] = (int(i))
		j+=1
	k+=1
data = np.array(arr1)


with open("DataLinked/Types2.csv", "w") as f:
	np.savetxt(f,data.astype(int), fmt='%i', delimiter = ',')

sys.exit()
