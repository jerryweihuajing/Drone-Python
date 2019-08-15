# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:56:31 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Object-drone4
"""

import copy as cp
import numpy as np
import matplotlib.pyplot as plt

from o_drone import drone
    
import Plot as Pl

#==============================================================================  
#Unmanned Aerial Vehicle (UAV) with 4 rotors
#==============================================================================  
class drone4(drone):
    def __init__(self,
                 size=None,
                 position_NED=None,
                 velocity_NED=None,
                 velocity_body=None,
                 attitude=None,
                 attitude_rate=None,
                 track=None,
                 is_arm=None,
                 is_in_air=None,
                 coordinate_takeoff_point=None):
        
        drone.__init__(self,
                       size=None,
                       position_NED=None,
                       velocity_NED=None,
                       velocity_body=None,
                       attitude=None,
                       attitude_rate=None,
                       track=None,
                       is_arm=None,
                       is_in_air=None,
                       coordinate_takeoff_point=None)
     
    def Update(self,waypoint,yaw):
        
        #way point position
        self.position_NED=np.array(waypoint)
        
        #collect it into track list
        self.track.append(self.position_NED)
        
        #yaw direction
        self.attitude=np.array([0,0,yaw])
        
    def Plot(self,ax,arrow=False,pole=False):
        
        yaw=self.attitude[2]
        
        #relative azimuth of rotors: 45° 135° -135° -45°
        relative_azimuth_rotors=[yaw+np.pi*(1+2*k)/4 for k in range(4)]

        #relative positions of rotors
        relative_position_rotors=[np.sqrt(2)/2*self.size*np.array([np.sin(this_azimuth),np.cos(this_azimuth),0])\
                                  for this_azimuth in relative_azimuth_rotors]
              
        #absolute positions
        position_rotors=[np.array(self.position_NED)+np.array(this_relative_position)\
                         for this_relative_position in relative_position_rotors]

        '''quadrangle method'''
        
        
        '''main frame'''
        main_frame_color='r'
        
        #main fram legs index
        map_index={}
        
        #head and tail position index
        map_index[0]=2
        map_index[1]=3
        
        #plot main frame
        for k in range(2):
            
            head_index=k
            tail_index=map_index[k]
            
            Pl.LinePlot(position_rotors[head_index],
                        position_rotors[tail_index],
                        main_frame_color,
                        ax)    
            
        '''rotors: need improvement'''   
        rotors_color='k'
        
        #different colors stand for different rotation direction
        position_rotors_anticlockwise=[position_rotors[0],position_rotors[2]]
        position_rotors_clockwise=[position_rotors[1],position_rotors[3]]
        
        #XY coordinates of red rotors
        x_coordinates_rotors_clockwise=[this_pos[0] for this_pos in position_rotors_clockwise]
        y_coordinates_rotors_clockwise=[this_pos[1] for this_pos in position_rotors_clockwise]
        
        #XY coordinates of black rotors
        x_coordinates_rotors_anticlockwise=[this_pos[0] for this_pos in position_rotors_anticlockwise]
        y_coordinates_rotors_anticlockwise=[this_pos[1] for this_pos in position_rotors_anticlockwise]
        
        #plot 4 rotors
        ax.plot(x_coordinates_rotors_clockwise,
                y_coordinates_rotors_clockwise,
                rotors_color+'.',
                markersize=13)   
        
        ax.plot(x_coordinates_rotors_anticlockwise,
                y_coordinates_rotors_anticlockwise,
                rotors_color+'.',
                markersize=13) 
        
        '''track'''
        #XY coordinates of track
        x_coordinates_track=[this_pos[0] for this_pos in self.track]
        y_coordinates_track=[this_pos[1] for this_pos in self.track]
        
        #plot track
        ax.plot(x_coordinates_track,y_coordinates_track,'b-')
        
        #plot arrow
        if arrow and self.is_in_air:
                
            arrow_color='g'
            
            '''arrow'''
            #arrow head and tail
            position_arrow_head=np.array(self.position_NED)+1.2*self.size*np.array([np.sin(yaw),np.cos(yaw),0])
            position_arrow_tail=np.array(self.position_NED)
            
            Pl.LinePlot(position_arrow_head,
                        position_arrow_tail,
                        arrow_color,
                        ax)  
            
            '''arrow wings'''
            #left wing end position
            position_arrow_wing_left=np.array(position_arrow_head)\
                                     -0.2*self.size*np.array([np.sin(yaw-np.pi/4),np.cos(yaw-np.pi/4),0])
            
            #right wing end position
            position_arrow_wing_right=np.array(position_arrow_head)\
                                     -0.2*self.size*np.array([np.sin(yaw+np.pi/4),np.cos(yaw+np.pi/4),0])
             
            #plot arrow wings
            Pl.LinePlot(position_arrow_head,
                        position_arrow_wing_left,
                        arrow_color,
                        ax) 
            
            Pl.LinePlot(position_arrow_head,
                        position_arrow_wing_right,
                        arrow_color,
                        ax)  
            
        #plot polar radius
        if pole and self.is_in_air:
            
            '''polar radius'''
            polar_radius_color='k'
            
            Pl.LinePlot(self.coordinate_takeoff_point,
                        self.position_NED,
                        polar_radius_color,
                        ax)
            
            '''pole'''
            pole_color='r'
            
            ax.plot([self.coordinate_takeoff_point[0]],
                    [self.coordinate_takeoff_point[1]],
                    pole_color+'.',
                    markersize=23) 
            