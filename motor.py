import pyrosim.pyrosim as pyrosim
import pybullet as p 
import constants as c 
import numpy as np

class MOTOR: 
    def __init__(self, jointName): 
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self): 
        self.amplitude = c.amplitudefrontleg
        self.frequency = c.frequencyfrontleg
        self.offset = c.phaseOffSetfrontleg
        self.motorValues = np.linspace(0, 2*np.pi, c.iterations)
        for x in range(c.iterations):
            self.motorValues[x] = self.amplitude * np.sin(self.frequency * self.motorValues[x] + self.offset)

    def Set_Value(self, robotId, time):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, 
        controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[time], maxForce = c.maxForce)

    def Save_Values(self):
        np.save("data/" + self.jointName, self.motorValues)