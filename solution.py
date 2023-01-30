import numpy as np 
import os 
import pyrosim.pyrosim as pyrosim
import random

class SOLUTION: 
    def __init__(self, nextAvailableID): 
        self.weights = (np.random.rand(3, 2) *2 ) - 1
        self.myID = nextAvailableID 
        
    def Set_ID(self, id): 
        self.myID = id

    def Evaluate(self, directOrGUI):
        pyrosim.Start_SDF("world.sdf")
        self.Create_World() 
        self.Generate_Body() 
        self.Generate_Brain() 
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " &")
        file = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(file.read())
        file.close()

    def Create_World(self): 
        pyrosim.Send_Cube(name="Box", pos=[-1,-1,.5] , size=[1,1,1])
        pyrosim.End() 
    
    def Generate_Body(self): 
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="frontleg", pos=[-0.5, 0, -0.5] , size=[1,1,1])
        pyrosim.Send_Joint(name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [2, 0, 1])
        pyrosim.Send_Cube(name="backleg", pos=[0.5, 0, -.5] , size=[1 ,1,1])
        pyrosim.End()

    def Generate_Brain(self): 
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "backleg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "frontleg")
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "torso_backleg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "torso_frontleg")

        for currentRow in range(3): 
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , 
                weight = self.weights[currentRow][currentColumn] )

        pyrosim.End()

    def Mutate(self): 
        self.weights[random.randint(0,2), random.randint(0,1)] = random.random() * 2 -1 
