# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:42:16 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-DISARM
"""

#------------------------------------------------------------------------------
"""
Drone unlocking

Args:
    which_drone: drone object which performs
    ax: axes where drone is plotted
    
Returns:
    None
"""  
def Disarm(which_drone,ax=None):
    
    print('')
    
    if which_drone.is_in_air:
        
        print('ERROR: the drone is still in flight!')
        
        return
    
    #unlock
    which_drone.is_arm=False
    
    print("-- Disarming")
   
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
