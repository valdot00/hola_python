# entrada y salida de arrays

import numpy as np

array1 = np.arange(6)

print(array1)

#array([1,2,3,4,5])

np.save('arrayls',array1)

np.load('arrayls.npy')

array1 = np.arange(6)

print(array1)

array2 = np.arange(8)

print(array2)

np.savez('arrays',x=array1,y=array2)

array_recuperado = np.load('arrays.nps')

print(array_recuperado['x'])

print(array_recuperado['y'])

np.savetxt('minificheroarray.txt',array2,delimiter=',')

np.loadtxt('minificheroarray.txt',delimiter=',')

