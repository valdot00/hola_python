# estadisticas en dataframes

from typing import List
import pandas as pd

import numpy as np

array = np.array([[1,8,3],[5,6,7]])

print(array)

datafreme = pd.DataFrame(array, index=['a','b'], columns=List('123'))

print(datafreme.sum())

print(datafreme.sum(axis=1))

print(datafreme.min())

print(datafreme.max(axis=1))

print(datafreme.idxmin())

print(datafreme)

print(datafreme.describe())