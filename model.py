#model.py

import numpy as np
import matplotlib.pyplot as plt

def read_neighbours(file:str):
    d = 0

class Node:
    def __init__(self, mark:bool=0, names:list):
        self.names = names
        self.mark = mark
        self.neighbours = np.array([], dtype=Node)
        
        read_neighbours(names[0])
        
