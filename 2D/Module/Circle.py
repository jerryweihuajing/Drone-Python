# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:03:32 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Circle
"""

import numpy as np

#------------------------------------------------------------------------------
"""
calculated points above a circle

Args:
    center: center position of circle
    radius: radius of circle
    start_azimuth: the azimuth where the circle start
    num: amounts of micro units which consist of circle
    rotation: circle point rotation direction
    
Returns:
    Position list of points which are above circle
"""
def PointsAboveCircle(center,radius,start_azimuth=0,num=1000,rotation='clockwise'):
    
    #to float
    center=np.array(center)
    radius=np.array(radius)
    
    '''lazy method: use points nearby or directional list method instead'''
    #rotation direction and angle 
    alpha=np.linspace(start_azimuth,start_azimuth+2*np.pi,num)
    
    #coordinates
    coordinates=[]

    #points above circle       
    for this_alpha in alpha:
        
        #polar coordinates
        this_pos=center+np.array([radius*np.sin(this_alpha),radius*np.cos(this_alpha)])
        
        #collect
        coordinates.append(this_pos)
        
    if rotation=='counter-clockwise':
        
        coordinates.reverse()
        
    return coordinates

#------------------------------------------------------------------------------
"""
Plot graphic object in an ax

Args:
    center: center position of circle
    radius: radius of circle
    ax: ax on which the circle is plotted
    
Returns:
    None
"""
def CirclePlot(center,radius,ax):
    
    #coordinates of points above circle
    coordinates=PointsAboveCircle(center,radius)
        
    #XY coordinates
    X_coordinates=[this_pos[0] for this_pos in coordinates]
    Y_coordinates=[this_pos[1] for this_pos in coordinates]
    
    #plot
    ax.plot(X_coordinates,Y_coordinates,'k')