# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:53:41 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：ACTION_LIB-WAYPOINT_FLIGHT
"""

import numpy as np

#------------------------------------------------------------------------------
"""
Drone flies to waypoint

(1) behavior_mode 0 : relative position local NED frame
params[0], params[1], params[2] → dx,dy,dz respectively

(2) behavior_mode 1: abs local NED
params[0], params[1], params[2] → x,y,z respectively.

For all modes, params[3] is yaw setpoint (unit in degree).

Args:
    which_drone: drone object which performs
    waypoint_params: waypoint information
    behavior_mode: absolute and relative flight mode
    ax: axes where drone is plotted
    
Returns:
    None
""" 
def WaypointFlight(which_drone,waypoint_params,behavior_mode=0,ax=None):
    
    if not which_drone.is_in_air:
        
        print('ERROR: the drone is not in flight!')
        
        return
    
    yaw=waypoint_params[3]
    
    #absolute mode
    if behavior_mode==0:
        
        #coordinate of destination point
        destination_x=waypoint_params[0]
        destination_y=waypoint_params[1]
        destination_z=waypoint_params[2]
        
        #destination point
        destination_position_ned=np.array([destination_x,destination_y,destination_z])
        
        print('')
        print("-- Go to waypoint absolutely within local coordinate NED system")
        print('-> Go to north %.2f (meter)'%waypoint_params[0])
        print('-> Go to east %.2f (meter)'%waypoint_params[1])
        print('-> Go to down %.2f (meter)'%waypoint_params[2])
        print('-> The yaw is %.2f (degree)'%(waypoint_params[3]*180/np.pi))
        
    #relative mode
    if behavior_mode==1:
        
        #coordinate difference
        difference_x=waypoint_params[0]
        difference_y=waypoint_params[1]
        difference_z=waypoint_params[2]
        
        #start point
        start_position_ned=which_drone.position_NED
        
        #destination point
        destination_position_ned=np.array([start_position_ned[0]+difference_x,
                                           start_position_ned[1]+difference_y,
                                           start_position_ned[2]+difference_z])
        
        print('')
        print("-- Go to waypoint relatively within local coordinate NED system")
        print('-> Go north %.2f (meter)'%waypoint_params[0])
        print('-> Go east %.2f (meter)'%waypoint_params[1])
        print('-> Go down %.2f (meter)'%waypoint_params[2])
        print('-> The yaw is %.2f (degree)'%(waypoint_params[3]*180/np.pi))
        
    which_drone.Update(destination_position_ned,yaw)
    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)