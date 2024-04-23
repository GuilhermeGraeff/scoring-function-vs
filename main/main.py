import sys
import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
from tabulate import tabulate
import math

# First of all, who starts a code with 'first of all', lmao
# If this project works, then we will have an awesome content, if it does not work, well, i tried it.

# Apparently doing something like the code bellow does not work(if class_2 knows how to time travel then it could work, probably there is an easy way to do it so :P):
#   class_1 = Stuff(class_2)
#   class_2 = Stuff(class_1)

class Program:
    def __init__(self):
        print('Program starting up.')
        self.misc = Mycelium(self)
        self.algs = Algorithms(self)
        print('Program is running.')

# Class destined to put miscellaneous stuff, like generators for unsorted vectors, sorted vectors(for search)
# The name is because Mycelium is the first thing that comes to mind when i think of Miscellaneous. 
class Mycelium:
    # I find great to use what we are developing here, so let's have this classes mixed together.
    def __init__(self, parent):
        self.utils = parent
        print('Mycelium is up and running.')


   
    def sortedVector(self, size, range):
        # 'size' INT is the vector length
        # 'range' Tuple(vector) is the range of values, from x to y, [x,y] 
        # for size = 10 and range = [2,18], this function returns -> [1,3,4,5,5,6,9,10,10,14]
        # if y - x < size the numbers will repeat more often (intuition)
        
        unsortedVector = self.unsortedVector(size, range)
        result = self.utils.algs.bubbleSort(unsortedVector)
        return result


    def unsortedVector(self, size, boundrie):
        # 'size' INT is the vector length
        # 'range' Tuple(vector) is the range of values, from x to y, [x,y] 
        # for size = 10 and range = [2,18], this function returns -> [9,3,14,5,2,10,1,18,10,4]
        # if y - x < size the numbers will repeat more often (intuition)

        result = []
        print(size)
        for x in range(0, size, 1):
            randomNumber = random.randrange(boundrie[0], boundrie[1])  
            result.append(randomNumber)
        return result
    
    def swap(self, vector, x, y):
        # simple swap by indexes using two variables

        vector[x] = vector[x] + vector[y]
        vector[y] = vector[x] - vector[y]
        vector[x] = vector[x] - vector[y]


class Algorithms:
    # ...classes mixed together.

    def __init__(self, parent):
        self.utils = parent
        print('Algorithms is up and running.')

    # This was a test:
    def bubbleSort(self, vector):
        swaped = True
        while swaped == True:
            swaped = False
            for i in range(0, len(vector) - 1, 1):
                if vector[i] > vector[i+1]:
                    self.utils.misc.swap(vector, i, i+1)
                    swaped = True
        return vector
    

    # Some function of x that land's on y as (3x² + 30x + 5):
    def f(self, x):
        return (3*(x**2)) + (30*x) + 5
    
    # Both graphs from f and f' are plotted in 1-image.png the images fol
    # The function above derivative ^v (6x + 30)
    def f_linha(self, x):
        return 6*x + 30

    # Gradient-based Optimization, using only 2 dimension (improve required)
    def gradientAscent(self, x, alpha, threshold):
        old_x = x
        run = True
        while run:
            x = x - (alpha * self.f_linha(x))
            print(old_x, x, self.f_linha(x))
            if abs((x - old_x)) < threshold:
                run = False
            old_x = x
        return x
    
    def newtonMethod(self, vector):
        return vector



def main() -> int:
    program = Program()

    vector = program.misc.unsortedVector(10, [2,15])
    print(vector)
    
    vector1 = program.misc.sortedVector(10, [2,15])
    print(vector1)

    slopeTopX = program.algs.gradientAscent(1, 0.01, 0.001)
    slopeTopY = program.algs.f(slopeTopX)
    print(slopeTopX, slopeTopY)


    return 0

if __name__ == '__main__':
    sys.exit(main()) 