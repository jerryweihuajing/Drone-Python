# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 14:57:18 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-WayPoints
"""

import numpy as np

import sys,os

import Geometry as Geom

#------------------------------------------------------------------------------
"""
Combine many waypoints list

Args:
    list_way_points: [waypoints1,waypoints1,...]
    
Returns:
    total_way_points
"""  
def CombineWayPoints(list_way_points):
    
    total_way_points=[]
    
    for k in range(len(list_way_points)-1):
    
        #way points between 2 way points list
        bridge_way_points=BridgeBetween2WayPoints(list_way_points[k],list_way_points[k+1])
               
        total_way_points+=list_way_points[k]
        total_way_points+=bridge_way_points

    #plus tail list
    return total_way_points+list_way_points[-1]

#------------------------------------------------------------------------------    
"""
Calculate Average distance of way points

Args:
    way_points: way points list
    
Returns:
    step length
"""   
def WayPointsAverageDistance(way_points):
    
    #The distance between two adjacent points
    way_points_distances=[Geom.Distance(way_points[k],way_points[k+1]) for k in range(len(way_points)-1)]
    
    return np.average(way_points_distances)
        
#------------------------------------------------------------------------------   
"""
Calculate way points list which perform A first then perform B

Args:
    way_points_A: way points list to perform first
    way_points_B: way points list to perform later
    
Returns:
    bridge way points between way oints A and way points B
"""
def BridgeBetween2WayPoints(way_points_A,way_points_B):
    
    #tail of A and head of B
    bridge_head=way_points_A[-1]
    bridge_tail=way_points_B[0]
    
    #distance between bridge_head and bridge_tail
    length_bridge=Geom.Distance(bridge_head,bridge_tail)
    
    #step length
    step_distance=WayPointsAverageDistance(way_points_A+way_points_B)
    
    #amount of bridge way points
    num_bridge_way_points=int(np.floor(length_bridge/step_distance))
    
    #xy diff
    xy_diff=(np.array(bridge_tail)-np.array(bridge_head))/(length_bridge/step_distance)
    
    return [np.array(bridge_head)+k*xy_diff for k in range(1,num_bridge_way_points)]
    