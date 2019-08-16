# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:06:46 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-TURN
"""

import copy as cp
import numpy as np

#------------------------------------------------------------------------------
"""
Drone turns its head

(1) behavior mode 0: abs yaw sp, params [0] value in radius unit

(2) behavior mode 1: relative yaw sp, params[0] rel yaw value in degrees

Args:
    which_drone: drone object which performs
    angle: degrees which is turn direction information
    behavior_mode: absolute and relative flight mode
    ax: axes where drone is plotted
        
Returns:
    None
""" 
def Turn(which_drone,angle,behavior_mode,ax=None):
    
    print('')
    
    if not which_drone.is_in_air:
        
        print('ERROR: the drone is not in flight!')
        
        return
    
    #absolute mode
    if behavior_mode==0:
        
        print("-- Turn to azimuth %.2f degrees absolutely"%angle)
        
        azimuth=cp.deepcopy(angle)
        
    #relative mode
    if behavior_mode==1:

        print("-- Turn %.2f degrees relatively"%angle)
        
        azimuth=which_drone.attitude[-1]+cp.deepcopy(angle)
        
    '''note: abs yaw value range [-180, 180] deg in NED frame'''
    while azimuth>180:
        
        azimuth-=2*180
    
    while azimuth<-180:
        
        azimuth+=2*180
    
    yaw=cp.deepcopy(azimuth)
    
    #update
    which_drone.Update(which_drone.position_NED,yaw*np.pi/180)
    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
