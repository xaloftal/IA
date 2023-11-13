import numpy as np

#matriz(tamanho)(probabilidade de obstaculos)
#PROBABILIDADE 30% de obstaculos

matrix2530 = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


matrix1030 = [
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
]



#PROBABILIDADE 25% de obstaculos

matriz4040 = [
    [[0 0 1 1 0 0 1 1 0 1 0 1 1 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 1 0 1 0 1 0 1 1 0 0 0 1 0 1 1 0 1 0 1 1 0 1 0 1
  0 0 0 0]
 [0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 1 0
  1 0 0 0]
 [1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0
  0 1 0 0]
 [0 0 1 1 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 0 1 0
  0 1 1 0]
 [0 0 0 1 1 0 1 0 0 0 1 1 0 0 0 1 0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 1 0 1
  0 1 0 0]
 [0 0 0 1 0 0 0 0 0 1 0 1 1 1 1 0 0 0 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 0
  1 1 0 1]
 [0 0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 1
  1 1 1 0]
 [0 1 0 1 1 0 1 0 0 1 1 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
  0 1 0 1]
 [1 0 1 1 0 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 1 0 1 0 1 1 0 1
  1 1 0 1]
 [1 0 0 0 0 0 1 1 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 0 1 0
  1 1 0 1]
 [1 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0
  1 0 0 0]
 [0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 1 0 1 1 0 1 0 1 0 0 0 0 0
  0 1 0 0]
 [0 1 1 1 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0
  0 0 0 1]
 [1 0 0 0 0 0 1 1 1 1 0 0 0 1 0 1 0 0 0 1 0 0 0 0 0 1 1 1 0 0 0 1 0 0 0 0
  0 0 1 1]
 [0 0 1 1 0 1 1 1 0 0 0 0 0 1 0 1 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0
  0 1 0 0]
 [0 1 0 1 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 1 0 0 1 0 0 0 0 0
  1 1 1 0]
 [0 0 0 0 0 0 0 1 0 0 0 0 1 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1
  0 0 0 1]
 [0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 1 0 1 1 0 1 1 0 0 0 1 1 0 0 0 0 1 0 1
  0 1 0 0]
 [0 0 1 1 1 1 1 0 0 1 1 1 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0
  0 0 0 0]
 [0 0 0 0 1 0 1 1 0 0 0 1 0 1 1 0 0 1 0 1 1 0 1 0 0 0 0 0 0 0 1 0 0 0 1 1
  0 0 0 0]
 [1 0 0 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 0 1 0 0 0 0
  1 0 0 0]
 [0 1 0 0 0 0 0 0 0 1 1 0 0 0 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 1 1 0
  0 1 1 0]
 [0 1 0 0 1 0 0 1 0 1 1 1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 1 0
  1 1 0 1]
 [1 0 0 0 0 0 0 0 0 1 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 1 1 1 0 0 0 1
  0 1 1 0]
 [1 1 0 0 0 0 0 1 0 0 1 0 0 0 1 1 1 0 1 0 0 1 1 0 0 0 0 0 0 1 1 0 0 1 0 1
  0 1 1 1]
 [0 1 1 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 1 1 1 0 1 0 0 0 1 0 0 0 0 1 0 0 0
  1 0 1 0]
 [0 1 0 1 0 0 0 1 0 1 1 0 0 1 0 0 0 0 1 0 1 0 0 0 0 1 0 0 1 1 0 0 0 1 1 1
  0 0 0 0]
 [0 0 1 0 0 0 0 0 0 1 1 1 0 1 0 0 0 0 0 0 0 0 1 1 1 1 0 1 0 0 0 1 0 0 1 0
  1 0 0 0]
 [0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 0 0 0 1 0 0 1 1 1 0 0 0 0 0 0
  0 0 1 1]
 [0 0 0 0 0 1 1 0 0 0 1 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0 0 1 1 0 0 1 1 1 1 0
  0 0 1 0]
 [1 0 1 0 1 1 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 1 1 0 1 0 0 0 0
  1 0 0 1]
 [0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0
  0 0 0 0]
 [0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0 0 0 0
  1 0 1 0]
 [0 1 0 1 1 1 1 0 0 1 1 0 1 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 0 1 1 1 1 0 0 1
  0 0 0 1]
 [1 0 0 1 0 1 0 0 0 0 1 0 0 1 1 1 0 0 1 1 0 0 1 1 0 1 1 1 0 1 0 1 0 1 0 0
  0 0 0 1]
 [0 1 1 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 1
  0 0 1 0]
 [0 1 1 1 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0
  0 1 0 0]
 [0 0 1 0 0 0 1 1 0 0 0 0 0 0 1 0 1 1 1 1 0 1 0 0 1 0 0 1 1 1 1 0 0 0 0 0
  0 0 1 0]
 [0 1 0 0 1 0 0 1 0 0 1 1 0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0
  1 0 0 1]]
    
]
