# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:15:18 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-ARM
"""

import copy as cp

#------------------------------------------------------------------------------
"""
Drone unlocking

Args:
    which_drone: drone object which performs
    ax: axes where drone is plotted
    
Returns:
    None
"""  
def Arm(which_drone,ax=None):
    
    #unlock
    which_drone.is_arm=True
    
    #Init drone
    which_drone.Update([0,0,0],0)
   
    print('')
    print("-- Arming")
   
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
    