import numpy as np

nspins = 10 

allup = np.zeros(nspins)
for i in range(nspins) : allup[i]=1

alldown = np.zeros(nspins)
for i in range(nspins) : alldown[i]=-1

alternating = np.zeros(nspins)
for i in range(nspins) : 
  if i%2==0 : alternating[i]=-1
  else : alternating[i]=1
