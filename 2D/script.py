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
import matplotlib.font_manager as fm

import sys,os

sys.path.append('../')
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\Module')
sys.path.append(os.getcwd()+'\\Object')
sys.path=list(set(sys.path))  
  
from o_drone import drone
from o_drone4 import drone4

import Error as Err
import Circle as Cir
import Algebra as Al
import Waypoints as Way
import Geometry as Geom
import Simulation as Sim
import Animation as Ani

from ACTION_LIB import ARM
from ACTION_LIB import TURN
from ACTION_LIB import TAKEOFF
from ACTION_LIB import WAYPOINT_FLIGHT
from ACTION_LIB import LAND
from ACTION_LIB import DISARM

r=66
num_step=166

'''create a mission module'''
#scatter abovr circle
A_circle_scatter=Cir.PointsAboveCircle([-r,+r],r,+np.pi/2,num_step,'clockwise')
B_circle_scatter=Cir.PointsAboveCircle([+r,-r],r,-np.pi/2,num_step,'counter-clockwise')

#combine them
waypoints=Way.CombineWaypoints([A_circle_scatter,B_circle_scatter])

#3D format
waypoints_3D=Geom.Coordinates2Dto3D(waypoints)
    
#a new drone
AMENG=drone4()

AMENG.size=15
AMENG.track=[]

#init yaw and start point
start_yaw=-np.pi/2
start_point=waypoints_3D[0]

AMENG.attitude=[0,0,start_yaw]
#AMENG.Update(start_point,start_yaw)

plt.ion()
fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111)

plt.cla()
ARM.Arm(AMENG,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
TAKEOFF.TakeOff(AMENG,ax=ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
WAYPOINT_FLIGHT.WaypointFlight(AMENG,[50,0,0,0],0,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
TURN.Turn(AMENG,-45,1,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
WAYPOINT_FLIGHT.WaypointFlight(AMENG,[50,-50,0,0],0,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)
 
plt.cla()
TURN.Turn(AMENG,45,1,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
WAYPOINT_FLIGHT.WaypointFlight(AMENG,[-50,-50,0,0],0,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)
 
plt.cla()
TURN.Turn(AMENG,45,1,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)
   
plt.cla()
WAYPOINT_FLIGHT.WaypointFlight(AMENG,[-50,50,0,0],0,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)
 
plt.cla()
TURN.Turn(AMENG,-45,1,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
LAND.Land(AMENG,ax=ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

plt.cla()
DISARM.Disarm(AMENG,ax)
plt.axis([-100,100,-100,100])
plt.pause(1)

#flight simulation
#Sim.VariantVelocitySimulation(AMENG,waypoints_3D)

#ani=Ani.VariantVelocityAnimation(AMENG,waypoints_3D,file_name='8-digit.mp4')
