import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append("./")
sys.path.append("../")

from config import *
from NetGenerator import *

if __name__ == "__main__":
    ng = NetGenerator(0)
    ng.new_nn([4, 7, 7, 5, 2], rc = True)