# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 23:00:20 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Animation
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.animation as animation

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Module import Error as Err
from Module import Geometry as Geom
from Module import Simulation as Sim

#title font
title_font=fm.FontProperties(fname=r"C:\Windows\Fonts\GILI____.ttf",size=20)
   
#------------------------------------------------------------------------------
"""
Animation of drone flight simulation controlling waypoints position

Args:
    which_drone: drone object which performs
    way_points_3D: way points list
    error_level: level of error
    time_step: time step of animation 
    gif_name: output video name
    
Returns:
    None
"""  
def VariantVelocityAnimation(which_drone,way_points_3D,error_level=0.5,time_step=0.01,gif_name=None):
        
    plt.ion()
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111)
    
    # Add new element to list with everything that changes between frames
    frame, = ax.plot([],[],animated=True)
    
    #each frame of gif
    imgs=[]
    
    for k in range(1,len(way_points_3D)):
        
        this_way_point=way_points_3D[k]
        
        #clean ax
        ax.cla()
        
        #start point this iteration
        start_point=which_drone.position_NED
           
        #create flight error
        destination_point=Err.WayPointError(start_point,this_way_point,0.5)
        
        #yaw in start point
        start_yaw=Geom.Azimuth(start_point,destination_point)
          
        #update position and plot
        which_drone.Update(destination_point,start_yaw)
        which_drone.Plot(ax)
          
        plt.axis(Sim.FlightField(way_points_3D)*1.1)
        plt.title('Drone Flight Simulation 2D: Variant Velocity',fontproperties=title_font)
        plt.pause(0.01)
        
        imgs.append([frame])
    
    #defien a animation object
    ani=animation.ArtistAnimation(fig, 
                                imgs, 
                                interval=100,  
                                repeat_delay=None,
                                repeat = False,    
                                blit=True)
    
    #save the gif
    if gif_name is None:
        
        return ani
    
    if gif_name is not None:
        
        ani.save(gif_name,writer='imagemagick')
