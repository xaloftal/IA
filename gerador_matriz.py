import numpy as np
import pandas as pd
import xlsxwriter


#create NumPy matrix of random integers
A = np.random.randint(0, 2, (8, 8))
print(A)

df = pd.DataFrame(A).T
df.to_excel(excel_writer = "matriz.xlsx")