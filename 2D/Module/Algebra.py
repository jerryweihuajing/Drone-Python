# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:13:06 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Algebra
"""

import numpy as np

#------------------------------------------------------------------------------   
'''
Generate 1 or -1 with the equal probability

Args:
    None
    
Returns:
    1 or -1
'''
def Sign():
    
    sign=-1
    
    #Blance distribution
    if np.random.random()>0.5:
        
        sign=1
        
    return sign