#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:10:09 2018

@author: adrien

"""
import numpy as np
import pandas as pd

# testing the tree search algorithm
# then the autodidatic algorithm
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# testing library :=
import unittest
import rubiksim.rubik as rbsim
import rubikML.tree_search as rbsea

class TestTreeSearch(unittest.TestCase):
    
    def setUp(self):
        self.rubik_solver = rbsea.TreeSearch()
    
    def test_solver(self):
        self.rubik_solver.main_random_solving(nb_DFS=4, nb_smooth=4)
        
        print("Solver find : " + str(self.rubik_solver.solution))
        print("Real find : " + str(self.rubik_solver.smooth))
    
# launching the test
if __name__ == '__main__':
   unittest.main()



