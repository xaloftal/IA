import numpy as np
import pandas as pd
import xlsxwriter


A = np.random.choice([0, 1], size = (40,40), p = [.7,.3])
np.set_printoptions(threshold=np.inf)
print(A)
#escrever matriz em excel
#df = pd.DataFrame(A).T
#df.to_excel(excel_writer = "matriz.xlsx")

#df = pd.read_excel("matriz.xlsx")
#a = df.to_numpy()
#print(a)