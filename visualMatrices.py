import matplotlib.pyplot as plt
import numpy as np
from matriz45 import *

def visualize_2d_array(array):
    plt.imshow(array, cmap='binary', interpolation='nearest')
    plt.show()
    
visualize_2d_array(matrix10045)