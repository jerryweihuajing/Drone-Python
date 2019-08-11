# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:29:38 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Error
"""

import numpy as np

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())

from Module import Algebra as Al

#------------------------------------------------------------------------------
"""
Generate flight error on way point

Args:
    start_point: coordinate of start point
    destination_point:  coordinate of destination point
    error_level: level of error
    
Returns:
    Way point with error
"""
def WayPointError(start_point,destination_point,error_level):

    #transform into np.array
    start_point=np.array(start_point)
    destination_point=np.array(destination_point)
    
    #coordinate difference
    coordinate_diff=[]
    
    for k in range(len(start_point)):
        
        #error factor
        error_factor=error_level*np.random.random()*Al.Sign()

        coordinate_diff.append((destination_point-start_point)[k]*error_factor)
           
    return destination_point+np.array(coordinate_diff)
