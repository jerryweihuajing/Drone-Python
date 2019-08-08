# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 14:38:23 2019

@author: Wei Huajing
@company: Ameng
@e-mail: jerryweihuajing@126.com

@title：execution script
"""

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

#absolute translantion
async def run_offb_ctrl_velocity_ned():
    """ Does Offboard control using velocity NED co-ordinates. """

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Go up 2 m/s")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, -2.0, 0.0))
    await asyncio.sleep(4)

    print("-- Go North 2 m/s, turn to face East")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(2.0, 0.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Go South 2 m/s, turn to face West")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(-2.0, 0.0, 0.0, 270.0))
    await asyncio.sleep(4)

    print("-- Go West 2 m/s, turn to face East")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, -2.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Go East 2 m/s")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 2.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Turn to face South")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 0.0, 180.0))
    await asyncio.sleep(2)

    print("-- Go down 1 m/s, turn to face North")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 1.0, 0.0))
    await asyncio.sleep(4)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")
        
loop = asyncio.get_event_loop()
loop.run_until_complete(run_offb_ctrl_velocity_ned())