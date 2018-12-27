#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:48:54 2018

@author: adrien

"""
import numpy as np
import pandas as pd

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rubiksim.rubik as rb

class solver_autodidactic:
    
    inverse_move = {0:2,1:3,2:0,3:1,4:6,5:7,6:4,7:5,8:10,9:11,10:8,11:9}
    
    def __init__(self):
        self.perfect_rubik = rb.rubik_cube().init_state
    
    def generate_training_dataset(self, nb_raws, nb_smooth_max):
        
        """
        Procedure to create the dataset
        - start from perfect cube
        - smooth
        - record 3 things : state, number of coup, previous coup
        """
        smooth_sequence = np.random.randint(0,12,nb_smooth_max)
        
        list_result = []
        
        for i in range(nb_raws):
            
            # we choose the number of random move
            nb_move = np.random.randint(1, nb_smooth_max)
            
            # initial state 
            state = np.copy(self.perfect_rubik)
            
            # random move :
            smooth_sequence = np.random.randint(0, 12, nb_move)
            
            # we randomized the move
            for index_move in smooth_sequence:
                state = rb.rubik_cube().move_cube(index_move, state)
                
            last_move = smooth_sequence[-1]
            
            list_result.append([state, nb_move, self.inverse_move[last_move]])
            
        return list_result

    
    def preprocessing_dataset(self, list_result, dropduplicates=True):
        """
        From the generated dataset we register :
        We look for data with the same state of the cube
        and we take the one with the better "number of coup"            
        """
        # we look at the same state in the dataset and we delete the one with the most number of move
        # TODO
        
        
        # now we preprocess the data to have a correct input into the neural network
        # Correct input :
        # - 3x3x6 -> 56x6 -> ~300 columns
        # And output :
        # - 1 the previous move : 12 columns (one hot auto_encoder)
        # - the value of the move : 1 column with integer / float
        
        list_array_flatten = []
        list_score = []
        list_todo_move = []
        
        for i in range(len(list_result)):
            array_noflatten = list_result[i][0]
            
            list_array_flatten.append(array_noflatten.flatten())    
            list_todo_move.append(list_result[i][2])
            list_score.append(list_result[i][1])
        
        # now we create the full array (so 3 array)
        array_state = np.array(list_array_flatten)
        array_todo = np.array(list_todo_move)
        array_score = np.array(list_score)
        
        if dropduplicates:
            # now we delete the double line (for state) taking the best move 
            unq, count = np.unique(array_state, axis=0, return_counts=True)
            
            # we get the dupliate raws :
            duplicates = unq[count>1]
            
            for raw in duplicates:
                data_index = np.where(array_state == raw)
                scores = array_score[data_index]
                
            
            
        
        # we concatenate our dataset
        
        
        
    def training_bootstrap_nn(self):
        
        """
        We train our neural network with our bootstap data :=)
        """
        # We load the dataset then we train our neural network on it
        # TODO

        pass
    
    
    
    







