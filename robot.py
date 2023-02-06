from sensor import SENSOR 
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT: 
    def __init__(self, solutionID): 
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("rm brain" + str(solutionID) + ".nndf")
        self.solutionID = solutionID

    def Prepare_To_Sense(self): 
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices: 
            self.sensors[linkName] = SENSOR(linkName)
    
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, time): 
        for sensor in self.sensors: 
            self.sensors[sensor].Get_Value(time)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName): 
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                jointName = self.nn.Get_Motor_Sensor_Joint(neuronName)
                self.motors[jointName].Set_Value(self.robotId, desiredAngle * c.motorJointRange)

    def Get_Fitness(self): 
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        #stateOfLinkZero = p.getLinkState(self.robotId, 0)
        #positionOfLinkZero = stateOfLinkZero[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]
        #file = open("fitness.txt", "w")
        file = open("tmp" + str(self.solutionID) + ".txt", "w")
        #file = open("tmp" + str(self.solutionID) + ".txt", "w")
        file.write(str(xPosition))
        file.close()
        os.system("mv tmp" + str(self.solutionID) + ".txt fitness" + str(self.solutionID) + ".txt")

    def Think(self):
        self.nn.Update()
        #self.nn.Print()



