# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:34:21 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Simulation
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import Error as Err
import Geometry as Geom

from ACTION_LIB import WAYPOINT_FLIGHT
from ACTION_LIB import ARM

#title font
title_font=fm.FontProperties(fname=r"C:\Windows\Fonts\GILI____.ttf",size=20)

#annotation font
annotation_font=fm.FontProperties(fname="C:\Windows\Fonts\GIL_____.ttf",size=16)

#------------------------------------------------------------------------------
"""
Calculate flight field

Args:
    way_points: way points list
    
Returns:
    [xmin,xmax,ymin,ymax]
"""    
def FlightField(way_points):
    
    #xy coordinates
    x_coordinates=[this_pos[0] for this_pos in way_points]
    y_coordinates=[this_pos[1] for this_pos in way_points]
    
    #boundary
    min_coordinate=np.min(x_coordinates+y_coordinates)
    max_coordinate=np.max(x_coordinates+y_coordinates)
    
    return np.array([min_coordinate,max_coordinate,min_coordinate,max_coordinate])

#------------------------------------------------------------------------------
"""
Drone flight simulation controlling waypoints position

Args:
    which_drone: drone object which performs
    way_points: way points list
    error_level: level of error
    time_step: time step of animation 
    
Returns:
    None
"""  
def VariantVelocitySimulation(which_drone,waypoints,error_level=0.5,time_step=0.01):
      
    plt.ion()
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111)

    #unlock the drone
    ARM.Arm(which_drone)
    
    if not which_drone.is_arm:
        
        print('ERROR: the drone is locked!')
        
        return
    
    for k in range(1,len(waypoints)):
        
        this_waypoint=waypoints[k]
        
        #clean ax
        ax.cla()
        
        #start point this iteration
        start_point=which_drone.position_NED
        
        #create flight error
        destination_point=Err.WayPointError(start_point,this_waypoint,error_level)
        
        #yaw in start point
        start_yaw=Geom.Azimuth(start_point,destination_point)
        
        #waypoint parameters
        this_waypoint_params=list(destination_point-start_point)+[start_yaw]
        
        #Waypoint flight
        WAYPOINT_FLIGHT.WaypointFlight(which_drone,this_waypoint_params,1)
        which_drone.Plot(ax,True,True)
    
        plt.axis(FlightField(waypoints)*1.1)
        plt.title('Drone Flight Simulation 2D: Variant Velocity',fontproperties=title_font)
        plt.pause(time_step)
        