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
    planned_way_points: ideal way point
    error_level: level of error (0-1)
    
Returns:
    Way point with error
"""
def WayPointError(planned_way_point,error_level):

    #create flight error
    error_way_point=[planned_way_point[0]*(1+error_level*np.random.random()*Al.Sign()),
                     planned_way_point[1]*(1+error_level*np.random.random()*Al.Sign()),
                     0]
    
    return error_way_point
