#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:30:07 2018

@author: adrien

"""
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rubiksim.rubik as rb

"""
This is a rubik ML solver !!!!!
"""

class TreeSearch:
    
    inverse_move = {0:2,1:3,2:0,3:1,4:6,5:7,6:4,7:5,8:10,9:11,10:8,11:9}
    solution = 0
    solve = 0
    
    def __init__(self, nb_smooth=3):
        self.nb_smooth = nb_smooth
        self.perfect_rubik = rb.rubik_cube().init_state

    def main_random_solving(self, nb_DFS, nb_smooth):
        
        smooth_rubik_  = self.smooth_rubik(np.copy(self.perfect_rubik), nb_smooth)
        
        self.solve_rubik(smooth_rubik_, nb_DFS, [])
        
                
        
    def solve_rubik(self, rubik_cube, nb_DFS, seq_move):
        
        if self.solve == 0:
            if np.array_equal(rubik_cube.state, self.perfect_rubik):
                print("solve !")
                print("solution :", str(seq_move))
                self.solution = seq_move
                self.solve = 1
            else:
                if nb_DFS != 0:
                    for i in range(12):        
                        self.solve_rubik(rubik_cube, nb_DFS-1, seq_move + [i])            
                
                # get the inverse move
                if seq_move != []:
                    previous_move = seq_move[-1]
                    
                    # calculate inverse move : TODO
                    inverse = self.move_inverse(previous_move)
                    rubik_cube.move(inverse)
                    
                
    def move_inverse(self, index_move):
        return self.inverse_move[index_move]
        
    
    def move_caract(self, move_index):
        pass
    
    def smooth_rubik(self, rubik_array, nb_smooth):
        
        rubik_ = rb.rubik_cube(rubik_array)
        
        smooth_sequence = np.random.randint(0,12,nb_smooth)
        self.smooth = smooth_sequence
        
        for i in smooth_sequence :
            rubik_.move(i)
        
        return rubik_
    
    
    
        
        
        
        
