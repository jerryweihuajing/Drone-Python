# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:15:55 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：Object-kinestate
"""

#==============================================================================  
#Initializes the VelocityBodyYawspeed object
#forward, right, down unit: m/s
#yawspeed unit: m/s
#==============================================================================  
class body_velocity_yaw_speed():
    def __init__(self,
                 forward=None,
                 right=None,
                 down=None,
                 yawspeed=None):
        self.forward=forward
        self.right=right
        self.down=down
        self.yawspeed=yawspeed