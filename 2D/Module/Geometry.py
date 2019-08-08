# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:08:26 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Geometry
"""

import numpy as np
 
#------------------------------------------------------------------------------
"""
Calculate the azimuth from start point to destination point
azimuth: The horizontal Angle between a point pointing north and the target direction

Args:
    start_point: coordinate of start point
    destination_point:  coordinate of destination point
    
Returns:
    Azimuth value(0-2*pi)
"""
def Azimuth(start_point,destination_point):
    
    #xy coordinate component
    x_component=start_point[0]-destination_point[0]
    y_component=start_point[1]-destination_point[1]
    
    #qudarant 1
    if x_component>0 and y_component>0:
        
        azimuth=np.arctan(np.abs(x_component)/np.abs(y_component))
    
    #qudarant 2
    if x_component>0 and y_component<0:
        
        azimuth=np.pi-np.arctan(np.abs(x_component)/np.abs(y_component))
     
    #qudarant 3
    if x_component<0 and y_component<0:
        
        azimuth=np.arctan(np.abs(x_component)/np.abs(y_component))+np.pi
    
    #qudarant 4
    if x_component<0 and y_component>0:
        
        azimuth=2*np.pi-np.arctan(np.abs(x_component)/np.abs(y_component))
        
    #North
    if x_component==0 and y_component>0:
        
        azimuth=0
    
    #South
    if x_component>0 and y_component==0:
        
        azimuth=np.pi/2
    
    #South
    if x_component==0 and y_component<0:
        
        azimuth=np.pi
        
    #West
    if x_component<0 and y_component==0:
        
        azimuth=3*np.pi/2
        
    return azimuth

#------------------------------------------------------------------------------
"""
Calculate the distance between 2 points based on coordinates

Args:
    pos_A: coordinate of point A 
    pos_B: coordinate of point B 
    
Returns:
    Distance between A and B
"""
def Distance(pos_A,pos_B):
  
    return np.sqrt(np.sum((np.array(pos_A)-np.array(pos_B))**2))  