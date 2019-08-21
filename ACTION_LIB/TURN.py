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
    angle_degree: anlge which is turn direction information (unit: degree)
    behavior_mode: absolute and relative flight mode
    ax: axes where drone is plotted
        
Returns:
    None
""" 
def Turn(which_drone,angle_degree,behavior_mode,ax=None):
    
    print('')
    
    if not which_drone.is_in_air:
        
        print('ERROR: the drone is not in flight!')
        
        return
    
    #absolute mode
    if behavior_mode==0:
        
        print("-- Turn to azimuth %.2f degrees absolutely"%angle_degree)
        
        azimuth_degree=cp.deepcopy(angle_degree)
        
    #relative mode
    if behavior_mode==1:

        print("-- Turn %.2f degrees relatively"%angle_degree)
        
        azimuth_degree=which_drone.attitude[-1]+cp.deepcopy(angle_degree)
        
    '''note: abs yaw value range [-180, 180] deg in NED frame'''
    while azimuth_degree>180:
        
        azimuth_degree-=2*180
    
    while azimuth_degree<-180:
        
        azimuth_degree+=2*180
    
    #degree to radian
    yaw_degree=cp.deepcopy(azimuth_degree)
    yaw_radian=yaw_degree*np.pi/180
    
    #update
    which_drone.Update(which_drone.position_NED,yaw_radian)
    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
