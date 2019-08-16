# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:06:35 2019

@title：ACTION_LIB-LAND
"""

import copy as cp

#------------------------------------------------------------------------------
"""
Drone takes off to height meters (default: 5)

Args:
    which_drone: drone object which performs
    ax: axes where drone is plotted
    
Returns:
    None
"""       
def Land(which_drone,ax=None):
    
    print('')
    
    if not which_drone.is_in_air:
        
        print('ERROR: the drone is not in flight!')
        
        return
    
    print("-- Land: Descend from altitude of height %.2f (meter)"%which_drone.position_NED[-1])
    
    #record land point position
    which_drone.coordinate_land_point=cp.deepcopy(which_drone.position_NED)
    which_drone.is_in_air=False
    
    print('-> Land point coordinate is [%.2f, %.2f, %.2f] (meter)'%(which_drone.coordinate_land_point[0],\
                                                                    which_drone.coordinate_land_point[1],\
                                                                    which_drone.coordinate_land_point[2]))
    print('-> Land point yaw is %.2f (degree)'%(which_drone.attitude[-1]))
    
    #Plot the drone
    if ax is not None:
        
        which_drone.Plot(ax,1,1)
