import numpy as np
from enum import Enum
import math as m

class Configuration:
    def __init__(self):

        # ---------------- COMMAND LIMITS ----------------
        self.max_x_velocity = 0.80
        self.max_y_velocity = 0.45
        self.max_yaw_rate = 1.25
        self.max_pitch = 30.0 * np.pi / 180.0

        # ---------------- FILTERING ----------------
        self.velocity_deadband = 0.25
        self.yaw_deadband = 0.25
        self.pitch_deadband = 0.05

        self.x_time_constant = 0.25
        self.y_time_constant = 0.25
        self.yaw_time_constant = 0.30
        self.pitch_time_constant = 0.25

        self.max_pitch_rate = 0.3
        self.roll_speed = 0.1
        self.z_speed = 0.06

        # ---------------- STANCE ----------------
        self.delta_x = 0.09
        self.delta_y = 0.085
        self.default_z_ref = -0.15
        self.z_clearance = 0.06

        # ---------------- GAIT ----------------
        self.dt = 0.01
        self.overlap_time = 0.04
        self.swing_time = 0.07

        # ---------------- GEOMETRY ----------------
        self.LEG_FB = 0.170
        self.LEG_LR = 0.0975
        self.L1 = 0.05162024721
        self.L2 = 0.11976
        self.L3 = 0.12518

        self.LEG_ORIGINS = np.array([
            [ self.LEG_FB,  self.LEG_FB, -self.LEG_FB, -self.LEG_FB],
            [-self.LEG_LR,  self.LEG_LR, -self.LEG_LR,  self.LEG_LR],
            [0.0, 0.0, 0.0, 0.0]
        ])

    @property
    def default_stance(self):
        x_row = np.array([ self.delta_x, self.delta_x, -self.delta_x, -self.delta_x ])
        y_row = np.array([-self.delta_y, self.delta_y, -self.delta_y, self.delta_y])
        z_row = np.array([ self.default_z_ref ] * 4)
        return np.vstack([x_row, y_row, z_row])
