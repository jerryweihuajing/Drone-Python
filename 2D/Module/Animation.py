# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:34:21 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Animation
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Module import Error as Err
from Module import Geometry as Geom

#title font
title_font=fm.FontProperties(fname=r"C:\Windows\Fonts\GILI____.ttf",size=20)

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
Drone flight simulation

Args:
    which_drone: drone object which performs
    way_points: way points list
    ax: ax on which the circle is plotted
    error_level: level of error (0-1)
    time_step: time step of animation 
    
Returns:
    None
"""  
def FlightSimulation(which_drone,way_points,ax,error_level=0.02,time_step=0.01):
    
    for this_way_point in way_points:
        
        #clean ax
        ax.cla()
        
        #start point this iteration
        start_point=which_drone.position_NED
        
        #create flight error
        destination_point=Err.WayPointError(this_way_point,error_level)
        
        #yaw in start point
        start_yaw=Geom.Azimuth(start_point,destination_point)
        
        #update position and plot
        which_drone.Update(destination_point,start_yaw)
        which_drone.Plot(ax)
    
        plt.axis(FlightField(way_points)*1.1)
        plt.title('Drone Flight Simulation 2D',fontproperties=title_font)
        plt.pause(time_step)

