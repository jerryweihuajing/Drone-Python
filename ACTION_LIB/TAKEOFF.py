# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:07:56 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-TAKEOFF
"""

import copy as cp

#------------------------------------------------------------------------------
"""
Drone takes off to height meters (default: 5)

Args:
    which_drone: drone object which performs
    start_position: coordinate of start point (default: [0,0])
    start_yaw: yaw of start point (default: 0)
    height: takeoff height (default: 5)
    ax: axes where drone is plotted
    
Returns:
    None
"""       
def TakeOff(which_drone,start_position=[0,0],start_yaw=0,height=5,ax=None):
    
    if not which_drone.is_arm:
        
        print('ERROR: the drone is locked!')
        
        return
    
    print('')
    print("-- Setting initial setpoint")
    
    #Init drone
    which_drone.Update([start_position[0],start_position[1],height],start_yaw)
    
    print('')
    print("-- Takeoff: Ascend to altitude of height (meter)")
    
    #record takeoff point position
    which_drone.coordinate_takeoff_point=cp.deepcopy(which_drone.position_NED)
    which_drone.is_in_air=True
    
    print('-> Takeoff point coordinate is [%.2f, %.2f, %.2f] (meter)'%(which_drone.coordinate_takeoff_point[0],\
                                                                       which_drone.coordinate_takeoff_point[1],\
                                                                       which_drone.coordinate_takeoff_point[2]))
    print('-> Takeoff point yaw is %.2f (degree)'%(which_drone.attitude[-1]))
    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
    