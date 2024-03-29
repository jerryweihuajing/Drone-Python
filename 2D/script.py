# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:42:59 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：execution script
"""

from __init__ import *

r=66
num_step=166

'''create a mission module'''
#scatter abovr circle
A_circle_scatter=Cir.PointsAboveCircle([-r,+r],r,+3*np.pi/4,num_step,'clockwise')
B_circle_scatter=Cir.PointsAboveCircle([+r,+r],r,-3*np.pi/4,num_step,'counter-clockwise')
C_circle_scatter=Cir.PointsAboveCircle([+r,-r],r,-np.pi/4,num_step,'counter-clockwise')
D_circle_scatter=Cir.PointsAboveCircle([-r,-r],r,+np.pi/4,num_step,'clockwise')

'''add return to launch'''
#combine them
waypoints=Way.CombineWaypoints([A_circle_scatter,
                                B_circle_scatter,
                                C_circle_scatter,
                                D_circle_scatter,
                                A_circle_scatter[:1]])

#3D format
waypoints_3D=Geom.Coordinates2Dto3D(waypoints)
    
#a new drone
AMENG=drone4()

AMENG.size=15
AMENG.track=[]

#init yaw and start point
#start_yaw=-np.pi/2
#start_point=waypoints_3D[0]
#
#AMENG.attitude=[0,0,start_yaw]

ARM.Arm(AMENG)
TAKEOFF.TakeOff(AMENG)

#ARM.Arm(AMENG,ax)
#AMENG.Update(start_point,start_yaw)
#
#plt.ion()
#fig=plt.figure(figsize=(8,8))
#ax=fig.add_subplot(111)
#
#plt.cla()
#ARM.Arm(AMENG,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#TAKEOFF.TakeOff(AMENG,ax=ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#WAYPOINT_FLIGHT.WaypointFlight(AMENG,[50,0,0,0],0,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#TURN.Turn(AMENG,-45,1,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#WPFLY_HEADLESS.WaypointFlightHeadless(AMENG,[1,1,1],ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#

#plt.cla()
#WAYPOINT_FLIGHT.WaypointFlight(AMENG,[50,-50,0,0],0,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
# 
#plt.cla()
#TURN.Turn(AMENG,45,1,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#WAYPOINT_FLIGHT.WaypointFlight(AMENG,[-50,-50,0,0],0,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
# 
#plt.cla()
#TURN.Turn(AMENG,45,1,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#   
#plt.cla()
#WAYPOINT_FLIGHT.WaypointFlight(AMENG,[-50,50,0,0],0,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
# 
#plt.cla()
#TURN.Turn(AMENG,-45,1,ax)
##plt.axis([-100,100,-100,100])
##plt.pause(1)
#
#plt.cla()
#LAND.Land(AMENG,ax=ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)
#
#plt.cla()
#DISARM.Disarm(AMENG,ax)
#plt.axis([-100,100,-100,100])
#plt.pause(1)

#flight simulation
#Sim.VariantVelocitySimulation(AMENG,waypoints_3D)

ani=Ani.VariantVelocityAnimation(AMENG,waypoints_3D,file_name='butterfly.mp4')
