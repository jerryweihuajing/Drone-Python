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

from Module import Circle as Cir
from Module import Algebra as Al
from Module import Geometry as Geom



plt.ion()
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)

r=66

#8 digit
#CirclePlot([-r,0],r,ax)
#CirclePlot([+r,0],r,ax)

Cir.CirclePlot([0,0],r,ax)

#scatter abovr circle
A_circle_scatter=Cir.PointsAboveCircle([+r,0],r,num=100,rotation='left')
B_circle_scatter=Cir.PointsAboveCircle([-r,0],r,num=100,rotation='right')

#combinge
way_points=B_circle_scatter+A_circle_scatter
 
AMENG=drone4()

AMENG.size=15
AMENG.track=[]

start_yaw=-np.pi/2

AMENG.attitude=[0,0,start_yaw]
AMENG.Update([0,0,0],start_yaw)

for k in range(len(way_points)):
    
    ax.cla()
    
    #start point this iteration
    start_point=AMENG.position_NED
    
#    create flight ERROR
#    destination_point=[way_points[k][0]*(1+0.01*np.random.random()*Al.Sign()),
#                       way_points[k][1]*(1+0.01*np.random.random()*Al.Sign()),
#                       0]
    
    destination_point=[way_points[k][0],way_points[k][1],0]
    
    #yaw in start point
    start_yaw=Geom.Azimuth(start_point,destination_point)
    
    AMENG.Update(destination_point,start_yaw)
    
    AMENG.Plot(ax)
    
    #ideal waypoints
#    ScatterPlot(circle_scatter,'r',ax)
    
    #ideal track
#    CirclePlot([+r,0],r,ax)
#    CirclePlot([-r,0],r,ax)

    plt.axis([-150,150,-150,150])

    plt.pause(0.01)
    