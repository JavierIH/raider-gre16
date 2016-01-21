import os
import sys
sys.path.append(os.path.abspath(__file__).replace('raider-gre16/raider.py', '') + 'pybotics/')

import time
import numpy as np
import math
import control.octosnake.octosnake as octosnake


class Raider(object):

    def __init__(self, servo_trims, servo_ids, name='raider'):

        # Configuration
        self._name = name
        self._servo_trims = servo_trims
        self._servo_ids = servo_ids


        # Setting up OctoSnake
        # self.osc = []
        # self.osc.append(octosnake.Oscillator())

    def back(self, steps, T=750.0):

        x_amp = 20
        z_amp = 15
        front_x = 8
        i = 0

        period = [T, T, T/2, T/2, T, T, T/2, T/2]
        amplitude = [x_amp, x_amp, z_amp, z_amp, x_amp, x_amp, z_amp, z_amp]
        offset = [front_x, front_x, -25, -25, front_x, front_x, -25, -25]
        phase = [270, 90, i, 270, 90, 270, i, i]

        for i in range(len(self.osc)):
            self.osc[i].period = period[i]
            self.osc[i].amplitude = amplitude[i]
            self.osc[i].phase = phase[i]
            self.osc[i].offset = offset[i]

        init_ref = time.time()
        final = init_ref + float(T*steps/1000)
        self.osc[0].ref_time = init_ref
        self.osc[1].ref_time = self.osc[0].ref_time
        self.osc[2].ref_time = self.osc[0].ref_time
        self.osc[3].ref_time = self.osc[0].ref_time
        self.osc[4].ref_time = self.osc[0].ref_time
        self.osc[5].ref_time = self.osc[0].ref_time
        self.osc[6].ref_time = self.osc[0].ref_time
        self.osc[7].ref_time = self.osc[0].ref_time
        while time.time() < final:
            side = int((time.time()-init_ref) / (T/2000.0)) % 2
            try:
                for i in range(len(self.osc)):
                    self.osc[i].refresh()

                self.controller.move(self._servo_pins[0], self.osc[0].output)
                self.controller.move(self._servo_pins[1], self.osc[1].output)
                self.controller.move(self._servo_pins[4], self.osc[4].output)
                self.controller.move(self._servo_pins[5], self.osc[5].output)
                if side == 0:
                    self.controller.move(self._servo_pins[3], -self.osc[3].output)
                    self.controller.move(self._servo_pins[6], -self.osc[3].output)
                else:
                    self.controller.move(self._servo_pins[2], self.osc[3].output)
                    self.controller.move(self._servo_pins[7], self.osc[3].output)

            except IOError:
                self._bus = smbus.SMBus(self._i2c_bu
