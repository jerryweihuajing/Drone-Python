# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:11:13 2019

@author: Wei Huajing
@company: Ameng Science and Technology Education Co., Ltd
@e-mail: jerryweihuajing@126.com

@title：initialization script
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
from ACTION_LIB import WPFLY_HEADLESS