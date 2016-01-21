import os
import sys
sys.path.append(os.path.abspath(__file__).replace('raider-gre16/raider.py', '') + 'pybotics/')

import time
import numpy as np
import math
import control.octosnake.octosnake as octosnake
import dynamixel

class Raider(object):

    def __init__(self, servo_trims, servo_ids, name='raider'):

        # Configuration
        self._name = name
        self._servo_trims = servo_trims
        self._servo_ids = servo_ids
        self.dxl = dynamixel.Dynamixel()


    def fake(self, steps, T=750.0):

        x_amp = 20
        z_amp = 15
        front_x = 8
        i = 0

        T = 500
        amplitude = 100
        offset = 612
        phase = 0

        osc = octosnake.Oscillator()

        osc.period = T
        osc.amplitude = amplitude
        osc.phase = phase
        osc.offset = offset

        init_ref = time.time()
        final = init_ref + float(T*steps/1000)
        while time.time() < final:
            osc.refresh()
            self.dxl.setPosition(6,int(osc.output))
            self.dxl.setPosition(4,int(osc.output))


robot = Raider(0,0)
robot.fake(3)
