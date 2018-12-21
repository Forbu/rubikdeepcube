#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 17:26:48 2018

@author: adrien

"""
import numpy as np
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# testing library :=
import unittest
import rubiksim.rubik as rb

class TestRubik(unittest.TestCase):

    def setUp(self):
        
        # init the rubik
        self.rubik_ = rb.rubik_cube()

    
    def test_init(self):
        pass
        
    def xtest_move_all(self):
        self.rubik_ = rb.rubik_cube()
        print("testing all the move")
        
        for i in range(12):
            self.rubik_.move(i)
            print(i)
            unique, counts = np.unique(self.rubik_.state, return_counts=True)
            print(dict(zip(unique, counts)))
        print(self.rubik_.state)

    def xtest_move(self):
        self.rubik_ = rb.rubik_cube()
        i = 8
        self.rubik_.move(i)
        print('move : ' + str(i))
        unique, counts = np.unique(self.rubik_.state, return_counts=True)
        print(dict(zip(unique, counts)))
        print(self.rubik_.state)

    def xtest_inverse_ok(self):
        
        self.rubik_ = rb.rubik_cube()
        i = 8
        print('move inverse ok : ' + str(i))
        self.rubik_.move(i)
        self.rubik_.move(i+2)
        
        print(self.rubik_.state)

    def test_random(self):
        
        self.rubik_ = rb.rubik_cube()
        
        for i in np.random.randint(0,12,10000):
            self.rubik_.move(i)
            
        print(self.rubik_.state)
        
        
    
    
 
# launching the test
if __name__ == '__main__':
   unittest.main()


