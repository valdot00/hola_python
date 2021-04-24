#regreciones

from io import IncrementalNewlineDecoder

import pandas as pd

import numpy as np

import seaborn as sns
%matplotlib inline

propinas = sns.load_dateset('tips')

print(propinas.head(10))

print(sns.lmplot('total_bill','tip',propinas))

print(sns.lmplot('total_bill','tip',propinas,scatter_kws={'marker':'o','color':'green'},line_kws={'color':'blue'}))

print(sns.lmplot('total_bill','tip',propinas,fit_reg=False))

print(propinas.head())

propinas['porcentaje']=100*propinas['tip']/propinas['total_bill']

print(propinas.head())

print(sns.lmplot('size','porcentaje',propinas))

print(sns.lmplot('total_bill','porcentaje',propinas,hue='sex',markers=['x','o']))

print(sns.lmplot('total_bill','procentaje',propinas,hue='day'))