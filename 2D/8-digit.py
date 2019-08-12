# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:42:59 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：execution script
"""

import copy as cp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Object.o_drone import drone
from Object.o_drone4 import drone4

from Module import Error as Err
from Module import Circle as Cir
from Module import Algebra as Al
from Module import WayPoints as WP
from Module import Geometry as Geom
from Module import Simulation as Sim
from Module import Animation as Ani

r=66
num_step=66

#scatter abovr circle
A_circle_scatter=Cir.PointsAboveCircle([-r,-r],r,+np.pi/2,num_step,'clockwise')
B_circle_scatter=Cir.PointsAboveCircle([+r,+r],r,-np.pi/2,num_step,'counter-clockwise')

#combine them
way_points=WP.CombineWayPoints([A_circle_scatter,B_circle_scatter])

#3D format
way_points_3D=Geom.Coordinates2Dto3D(way_points)
    
#a new drone
AMENG=drone4()

AMENG.size=15
AMENG.track=[]

#init yaw and start point
start_yaw=-np.pi/2
start_point=way_points_3D[0]

AMENG.attitude=[0,0,start_yaw]
AMENG.Update(start_point,start_yaw)

#flight simulation
#Sim.VariantVelocitySimulation(AMENG,way_points_3D)

Ani.VariantVelocityAnimation(AMENG,way_points_3D)
