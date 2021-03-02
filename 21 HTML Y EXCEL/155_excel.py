# ficheros formato Excel

import pandas as pd

fichero_excel = pd.ExcelFile('C:\Users\PC\Desktop\jorge_oswaldo_pelayo_arellano\python\21 HTML Y EXCEL\TABLAPYTHON.ods')

misdatosexcel = fichero_excel.parse('hoja1')

print(misdatosexcel)