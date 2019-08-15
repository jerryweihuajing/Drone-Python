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

import matplotlib
matplotlib.use('Qt5Agg')

import Error as Err
import Geometry as Geom
import Simulation as Sim

#title font
title_font=fm.FontProperties(fname=r"C:\Windows\Fonts\GILI____.ttf",size=20)
 
#------------------------------------------------------------------------------  
"""
Animation of drone flight simulation controlling waypoints position

Args:
    index: iteration index
    frame: frame object
    which_drone: drone object which performs
    waypoints_3D: way points list
    ax: ax which will be plotted
    error_level: level of error
    time_step: time step of animation 
    
Returns:
    None
"""  
def UpdateFrame(index,frame,which_drone,waypoints_3D,ax,error_level=0.5,time_step=0.01):
    
    try:
        
        this_waypoint=waypoints_3D[index+1]
            
        #clean ax
        ax.cla()
        
        #start point this iteration
        start_point=which_drone.position_NED
           
        #create flight error
        destination_point=Err.WayPointError(start_point,this_waypoint,error_level)
        
        #yaw in start point
        start_yaw=Geom.Azimuth(start_point,destination_point)
          
        #update position and plot
        which_drone.Update(destination_point,start_yaw)
        which_drone.Plot(ax)
          
        plt.axis(Sim.FlightField(waypoints_3D)*1.1)
        plt.title('Drone Flight Simulation 2D: Variant Velocity',fontproperties=title_font)
        plt.pause(time_step)
            
        return frame,
    
    except IndexError:
        
        return  frame,

#------------------------------------------------------------------------------
"""
Animation of drone flight simulation controlling waypoints position

Args:
    which_drone: drone object which performs
    waypoints_3D: way points list
    error_level: level of error
    time_step: time step of animation 
    file_name: output video name
    
Returns:
    None
"""  
def VariantVelocityAnimation(which_drone,waypoints_3D,error_level=0.5,time_step=0.01,file_name=None):
        
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=2000)
    
    plt.ion()
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111)
        
    # Add new element to list with everything that changes between frames
    frame, = ax.plot([],[])
    
    #create an animation
    ani = animation.FuncAnimation(fig,
                                   UpdateFrame,
                                   len(waypoints_3D)-1,
                                   fargs=(frame,
                                           which_drone,
                                           waypoints_3D[1:],
                                           ax),
                                   interval=10, 
                                   repeat = False,   
                                   blit=True)
                                   
    #save it
    if file_name!=None:
                
        ani.save(file_name, writer=writer)