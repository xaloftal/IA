import numpy as np
import pandas as pd
import xlsxwriter


#criar matriz aleatória com 0 e 1
#A = np.random.randint(0, 2, (8, 8))
#print(A)

A = np.random.choice([0, 1], size = (40,40), p = [.75,.25])
print(A)

#escrever matriz em excel
#df = pd.DataFrame(A).T
#df.to_excel(excel_writer = "matriz.xlsx")

#df = pd.read_excel("matriz.xlsx")
#df.as_matrix()