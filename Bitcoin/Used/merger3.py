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
Tipos3 = open ("Bitcoin3/Types3.csv","r")
for line in Tipos3.readlines():
	arr1.append([0 for x in range(6)])
	j = 0
	for i in ast.literal_eval(line):
		arr1[k][j] = (int(i))
		j+=1
	k+=1
Types3 = np.array(arr1)

arr2 = []
k = 0
Tipos3p2 = open ("Bitcoin3/Types3parte2.csv","r")
for line in Tipos3p2.readlines():
	arr2.append([0 for x in range(6)])
	j = 0
	for i in ast.literal_eval(line):
		arr2[k][j] = (int(i))
		j+=1
	k+=1
arr2 = np.array(arr2)
Types3p2 = np.column_stack((arr2.T[0], arr2.T[2], arr2.T[3], arr2.T[1], arr2.T[4], arr2.T[5] ))


ldat = len(Types3[0])
data = [[] for x in range(ldat)]


for column in range(ldat):
	data[column] = np.concatenate( (Types3.T[column], Types3p2.T[column]) )
#	data[column] = np.concatenate( (data1.T[column], data2.T[column], data3.T[column], data4.T[column]) )

data = np.array(data).T

with open("DataLinked/Types3.csv", "w") as f:
	np.savetxt(f,data.astype(int), fmt='%i', delimiter = ',')

sys.exit()
