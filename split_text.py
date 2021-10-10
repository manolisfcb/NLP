import numpy as np
import math

def split_text(text, n=10):
    '''Esta funcion recive una cadena de texto y la divide en n partes iguales'''
    length = len(text)
    size = math.floor(length/n)
    start = np.arange(0,length,size)
    split_list = []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece]+size])
    return split_list