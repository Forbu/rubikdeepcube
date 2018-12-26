#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:57:51 2018

@author: adrien

"""
import numpy as np
import pandas as pd

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rubiksim.rubik as rb

class mcts_solver:
    
    def __init__(self):
        pass
    
    def load_bootstrap(self):
        """
        We load our bootstrap solver (autodidactic)
        """
        pass
    
    def retrain_solve(self):
        """
        A lot of step here :
            - code the MCTS (we explore with a search tree)
            - we retrain our networks with the results of the search tree
        """
        pass
    


