#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:50:23 2018

@author: adrien

"""
import numpy as np
import pandas as pd

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rubiksim.rubik as rb

# testing library :=
import unittest
import rubiksim.rubik as rbsim
import rubikML.tree_search as rbsea
import rubikML.bootstrap_training as bo

class TestBoostrap(unittest.TestCase):
    
    def setUp(self):
        self.rubik_solver = bo.solver_autodidactic()
    
    def test_generate_training_dataset(self):
        
        list_result = self.rubik_solver.generate_training_dataset(10000, 3)
        self.rubik_solver.preprocessing_dataset(list_result)
        
    
# launching the test
if __name__ == '__main__':
   unittest.main()


