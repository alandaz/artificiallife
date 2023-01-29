from sensor import SENSOR 
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT: 
    def __init__(self): 
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Get_Fitness(self): 
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        file = open("fitness.txt", "w")
        file.write(str(xCoordinateOfLinkZero))
        file.close()

    def Think(self):
        self.nn.Update()
        #self.nn.Print()



