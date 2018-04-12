import numpy as np
import random
from pylab import *
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import math
import ast
import sys


data1 = np.loadtxt("DataLinked/Types" + '1.csv', delimiter = ',')
data2 = np.loadtxt("DataLinked/Types" + '2.csv', delimiter = ',')
data3 = np.loadtxt("DataLinked/Types" + '3.csv', delimiter = ',')
data4 = np.loadtxt("DataLinked/Types" + '4.csv', delimiter = ',')

l1 = len(data1.T[0])
l4 = len(data4.T[0])

Types1 = np.column_stack( (data1.T[1], data1.T[0], data1.T[4], data1.T[3], data1.T[2], [0 for x in range(l1)] ))
Types3 = np.column_stack( (data3.T[0], data3.T[4], data3.T[3], data3.T[2], data3.T[5], data3.T[1] ))
Types4 = np.column_stack( (data4.T[1], data4.T[4], data4.T[0], data4.T[3], [0 for x in range(l4)], data4.T[2] ))

with open("DataLinked/new/Types1.csv", "w") as f:
	np.savetxt(f, Types1.astype(int), fmt='%i', delimiter = ',')

with open("DataLinked/new/Types3.csv", "w") as f:
	np.savetxt(f, Types3.astype(int), fmt='%i', delimiter = ',')

with open("DataLinked/new/Types4.csv", "w") as f:
	np.savetxt(f, Types4.astype(int), fmt='%i', delimiter = ',')


ldat = len(data3[0])
data = [[] for x in range(ldat)]

for column in range(ldat):
	data[column] = np.concatenate( (Types1.T[column], data2.T[column], Types3.T[column], Types4.T[column]) )

#T2= [u'pubkeyhash', u'pubkey', u'scripthash', u'multisig', u'nonstandard', u'nulldata']
#T1 = [u'pubkey', u'pubkeyhash', u'nonstandard', u'multisig', u'scripthash']
#T3 = [u'pubkeyhash', u'nulldata', u'multisig', u'scripthash', u'pubkey', u'nonstandard']
#T4 = [u'scripthash', u'pubkeyhash', u'nulldata', u'multisig', u'pubkey']

data = np.array(data).T

with open("DataLinked/TypesTotal.csv", "w") as f:
	np.savetxt(f,data.astype(int), fmt='%i', delimiter = ',')

print len(data), len(data[0])
sys.exit()
