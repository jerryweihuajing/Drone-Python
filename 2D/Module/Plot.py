# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:06:56 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Module-Plot
"""

import numpy as np

#------------------------------------------------------------------------------
"""
Plot line with 2 points coordinate

Args:
    pos_A: point A coordinate
    pos_B: point B coordinate
    color: plot in which color
    ax: ax on which the circle is plotted
    
Returns:
    None
"""
def LinePlot(pos_A,pos_B,color,ax):
    
    #XY coordinates of 2 points
    x_coordinates=[pos_A[0],pos_B[0]]
    y_coordinates=[pos_A[1],pos_B[1]]
    
    ax.plot(x_coordinates,y_coordinates,color=color,linestyle='-')
    
#------------------------------------------------------------------------------
"""
Plot graphic object in an ax depending on coordinated

Args:
    coordinates: coordinates of points to be plotted
    color: plot in which color
    ax: ax on which the circle is plotted
    
Returns:
    None
"""
def ScatterPlot(coordinates,color,ax):
    
    #XY coordinates
    X_coordinates=[this_pos[0] for this_pos in coordinates]
    Y_coordinates=[this_pos[1] for this_pos in coordinates]
    
    #scatter point size
    scatter_size=(np.max(X_coordinates)-np.min(X_coordinates))/6
    
    #plot
    ax.plot(X_coordinates,
            Y_coordinates,
            color=color,
            marker='.',
            linestyle='',
            markersize=scatter_size)