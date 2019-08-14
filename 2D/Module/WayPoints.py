# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:57:18 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-WayPoints
"""

import numpy as np

import Geometry as Geom

#------------------------------------------------------------------------------
"""
Combine many waypoints list

Args:
    list_waypoints: [waypoints1,waypoints1,...]
    
Returns:
    total_waypoints
"""  
def CombineWaypoints(list_waypoints):
    
    total_waypoints=[]
    
    for k in range(len(list_waypoints)-1):
    
        #way points between 2 way points list
        bridge_waypoints=BridgeBetween2Waypoints(list_waypoints[k],list_waypoints[k+1])
               
        total_waypoints+=list_waypoints[k]
        total_waypoints+=bridge_waypoints

    #plus tail list
    return total_waypoints+list_waypoints[-1]

#------------------------------------------------------------------------------    
"""
Calculate Average distance of waypoints

Args:
    which_waypoints: waypoints list
    
Returns:
    step length
"""   
def WaypointsAverageDistance(which_waypoints):
    
    #The distance between two adjacent points
    waypoints_distances=[Geom.Distance(which_waypoints[k],which_waypoints[k+1]) for k in range(len(which_waypoints)-1)]
    
    return np.average(waypoints_distances)
        
#------------------------------------------------------------------------------   
"""
Calculate waypoints list which perform A first then perform B

Args:
    waypoints_A: way points list to perform first
    waypoints_B: way points list to perform later
    
Returns:
    bridge waypoints between way oints A and way points B
"""
def BridgeBetween2Waypoints(waypoints_A,waypoints_B):
    
    #tail of A and head of B
    bridge_head=waypoints_A[-1]
    bridge_tail=waypoints_B[0]
    
    #distance between bridge_head and bridge_tail
    length_bridge=Geom.Distance(bridge_head,bridge_tail)
    
    #step length
    step_distance=WaypointsAverageDistance(waypoints_A+waypoints_B)
    
    #amount of bridge way points
    num_bridge_waypoints=int(np.floor(length_bridge/step_distance))
    
    #xy diff
    xy_diff=(np.array(bridge_tail)-np.array(bridge_head))/(length_bridge/step_distance)
    
    return [np.array(bridge_head)+k*xy_diff for k in range(1,num_bridge_waypoints)]
    