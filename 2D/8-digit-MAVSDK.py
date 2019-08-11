# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:38:23 2019

@author: Wei Huajing
@company: Ameng
@e-mail: jerryweihuajing@126.com

@title：execution script
"""

import sys,os

if os.getcwd() not in sys.path:
    
    sys.path.append(os.getcwd())
    
from Module import Circle as Cir
from Module import Geometry as Geom

import asyncio

from mavsdk import start_mavlink
from mavsdk import connect as mavsdk_connect
from mavsdk import (
    Attitude,
    OffboardError,
    PositionNEDYaw,
    VelocityBodyYawspeed,
    VelocityNEDYaw,
)

start_mavlink()
drone = mavsdk_connect(host="127.0.0.1")

#fly to destination straightly
async def PositionNEDController():
    """ Does Offboard control using position NED co-ordinates. """
    
    height=5
    radius=5
    start_point=[0,0,0]
    start_yaw=0
    
    center=[0,-radius]
    way_points=Cir.PointsAboveCircle(center,radius,num=10)
    
    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNEDYaw(start_point[0],
                                                         start_point[1],
                                                         0.0,
                                                         start_yaw))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Takeoff: Ascend to altitude of height (m)")
    await drone.offboard.set_position_ned(PositionNEDYaw(start_point[0],
                                                         start_point[1],
                                                         -height,
                                                         start_yaw))
    await asyncio.sleep(10)

    print("-- Iteration: Cruise within local coordinate system")
    for k in range(len(way_points)-1):
        
        
        #start point this iteration
        start_point=way_points[k]
        
        #create flight error
        destination_point=way_points[k+1]
        
        #yaw in start point
        start_yaw=Geom.Azimuth(start_point,destination_point)
        
        await drone.offboard.set_position_ned(PositionNEDYaw(destination_point[0],
                                                             destination_point[1],
                                                             -height,
                                                             start_yaw))
        await asyncio.sleep(5)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")
        
loop = asyncio.get_event_loop()
loop.run_until_complete(PositionNEDController())