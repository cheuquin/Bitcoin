import numpy as np
import random
from pylab import *
from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import math
import ast
import sys


arr1 = []
k = 0
TiposF = open ("BitcoinRecent/TypesFinal.csv","r")
for line in TiposF.readlines():
	arr1.append([0 for x in range(7)])
	j = 0
	for i in ast.literal_eval(line):
		arr1[k][j] = (int(i))
		j+=1
	k+=1

data1 = np.array(arr1)
l1 = len(data1.T[0])

#T2= [u'pubkeyhash', u'pubkey', u'scripthash', u'multisig', u'nonstandard', u'nulldata']
#TF = [u'pubkeyhash', u'scripthash', u'witness_v0_scripthash', u'nulldata', u'witness_v0_keyhash', u'pubkey', u'multisig']

TypesF = np.column_stack( (data1.T[0], data1.T[5], data1.T[1], data1.T[6], [0 for x in range(l1)], data1.T[3], data1.T[2], data1.T[4] ))

with open("DataLinked/TypesFinal.csv", "w") as f:
	np.savetxt(f, TypesF.astype(int), fmt='%i', delimiter = ',')


sys.exit()
