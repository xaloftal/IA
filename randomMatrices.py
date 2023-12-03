import numpy as np

A = np.random.choice([0, 1], size=(1000, 1200), p=[0.5, 0.5])

# Convert array elements to strings and join with commas
matrix = np.array2string(A, separator=',', formatter={'int': lambda x: f'{x:,}'})


with open('outputMatrix.txt', 'w') as file:
    file.write('[')
    for i, row in enumerate(A):
        row_str = ', '.join(map(str, row))
        file.write(f'[{row_str}]' + (', ' if i < len(A) - 1 else '') + '\n')
    file.write(']')
    
