# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:18:51 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-WPFLY_HEADLESS
"""

import numpy as np

#------------------------------------------------------------------------------
"""
Drone flies to waypoint headlessly

params[0], params[1], params[2]  dx,dy,dz respectively in headless NED frame

• Headless mode, support human voice control
(forward, backward, leftward, rightward, ascend, descend voice msg).

• Yaw is kept with current yaw measurement (unit in deg).

Args:
    which_drone: drone object which performs
    waypoint_params: waypoint information
    ax: axes where drone is plotted
    
Returns:
    None
""" 
def WaypointFlightHeadless(which_drone,waypoint_params,ax):
    
    print('')
    
    if not which_drone.is_in_air:
        
        print('ERROR: the drone is not in flight!')
        
        return

    print(which_drone.position_NED)
    print(which_drone.coordinate_takeoff_point)
    
#    #coordinate difference
#    difference_x=waypoint_params[0]
#    difference_y=waypoint_params[1]
#    difference_z=waypoint_params[2]
#    
#    #start point
#    start_position_ned=which_drone.position_NED
#    
#    #destination point
#    destination_position_ned=np.array([start_position_ned[0]+difference_x,
#                                       start_position_ned[1]+difference_y,
#                                       start_position_ned[2]+difference_z])
#    '''import azimuth'''
#    '''+-: forward, backward, leftward, rightward, ascend, descend'''
#    print("-- Go to waypoint relatively within local coordinate NED system")
#    print('-> Go north %.2f (meter)'%waypoint_params[0])
#    print('-> Go east %.2f (meter)'%waypoint_params[1])
#    print('-> Go down %.2f (meter)'%waypoint_params[2])
#    print('-> The yaw is %.2f (degree)'%(waypoint_params[3]*180/np.pi))
#        
#    #yaw: unchanged
#    which_drone.Update(destination_position_ned,which_drone.atitude[-1])
#    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)