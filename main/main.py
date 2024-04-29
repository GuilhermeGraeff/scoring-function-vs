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

    def __init__(self, parent):
        self.utils = parent
        print('Mycelium is up and running.')

    def templateFunction(self, param_one, param_two):
        # Document Stuff

        do_stuff_here = param_one + param_two
        
        return do_stuff_here


class Algorithms:

    def __init__(self, parent):
        self.utils = parent
        print('Algorithms is up and running.')

    def templateFunction(self, vector):
        print("---")
        return vector


def main() -> int:
    program = Program()

    print()
    return 0


if __name__ == '__main__':
    sys.exit(main()) 