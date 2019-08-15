# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:56:31 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Object-drone
"""

#============================================================================== 
#Initializes the drone object
#position_NED: [pos_x,pos_y,pos_z]
#velocity_NED: [velocity_north,velocity_east,velocity_down]
#velocity_body: [velocity_forward,velocity_right,velocity_vertical]
#attitude: [roll,pitch,yaw]
#attitude_rate: [roll_rate,pitch_rate,yaw_rate]
#track: [position_1,position_2,...]
#============================================================================== 
class drone():
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
        self.size=size 
        self.position_NED=position_NED
        self.velocity_NED=velocity_NED
        self.velocity_body=velocity_body
        self.attitude=attitude
        self.attitude_rate=attitude_rate
        self.track=track
        self.is_arm=is_arm
        self.is_in_air=is_in_air
        self.coordinate_takeoff_point=coordinate_takeoff_point
