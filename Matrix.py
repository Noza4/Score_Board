import Data
import numpy as np 
import random


def build_up():
    rows = 6
    columns = 100
    matrix = np.empty((columns, rows), dtype="U50")

    for i in range(1, 100):
        matrix[i, 0] = Data.students[i]

    for i in range(1, 6):
        matrix[0, i] = Data.subjects[i - 1]

    for row in range(1, 100):
        for column in range(1, 6):
            matrix[row, column] = str(random.randint(1, 100))

    return matrix
            
    