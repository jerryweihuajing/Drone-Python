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

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Object.o_drone import drone
from Object.o_drone4 import drone4

from Module import Error as Err
from Module import Circle as Cir
from Module import Algebra as Al
from Module import Geometry as Geom
from Module import Animation as Ani

plt.ion()
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)

r=66

#8 digit
#CirclePlot([-r,0],r,ax)
#CirclePlot([+r,0],r,ax)

Cir.CirclePlot([0,0],r,ax)

'''need revision'''
#scatter abovr circle
A_circle_scatter=Cir.PointsAboveCircle([+r,0],r,num=100,rotation='left')
B_circle_scatter=Cir.PointsAboveCircle([-r,0],r,num=100,rotation='right')

#combine
way_points=B_circle_scatter+A_circle_scatter
 
AMENG=drone4()

AMENG.size=15
AMENG.track=[]

#init yaw and start point
start_yaw=-np.pi/2
start_point=[0,0,0]

AMENG.attitude=[0,0,start_yaw]
AMENG.Update(start_point,start_yaw)

#flight simulation
Ani.FlightSimulation(AMENG,way_points,ax)
    