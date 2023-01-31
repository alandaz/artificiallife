import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(9, 8) * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGui):
        pyrosim.Start_SDF("world.sdf")
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " 2&>1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessString = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessString):
            time.sleep(0.01)

        f = open(fitnessString, "r")
        self.fitness = float(f.read())
       # print(self.fitness)
        f.close()

        os.system("rm " + fitnessString)

    def Evaluate(self, directOrGui):
        pass
        

    def Create_World(self):
        pyrosim.Send_Cube(name="Box", pos=[-2,-2,.5] , size=[1,1,1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="torso", pos=[0, 0, 1] , size=[1, 1, 1])
        pyrosim.Send_Joint(name = "torso_frontleg" , parent= "torso" , 
        child = "frontleg" , type = "revolute", position = [0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontleg", pos=[0, 0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "frontleg_frontleg2" , parent= "frontleg" , 
        child = "frontleg2" , type = "revolute", position = [0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontleg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "torso_backleg" , parent= "torso" , child = "backleg" , 
        type = "revolute", position = [0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="backleg", pos=[0, -0.5, 0] , size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name = "backleg_backleg2" , parent= "backleg" , 
        child = "backleg2" , type = "revolute", position = [0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="backleg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "torso_leftleg" , parent= "torso" , child = "leftleg" , 
        type = "revolute", position = [-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="leftleg", pos=[-.5, 0, 0] , size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name = "leftleg_leftleg2" , parent= "leftleg" , 
        child = "leftleg2" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="leftleg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name = "torso_rightleg" , parent= "torso" , 
        child = "rightleg" , type = "revolute", position = [0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="rightleg", pos=[.5, 0, 0] , size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name = "rightleg_rightleg2" , parent= "rightleg" , 
        child = "rightleg2" , type = "revolute", position = [1, 0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="rightleg2", pos=[0, 0, -.5] , size=[0.2, 0.2, 1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "backleg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "frontleg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "leftleg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "rightleg")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName="frontleg2")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName="backleg2")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName="leftleg2")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName="rightleg2")

        pyrosim.Send_Motor_Neuron(name = 9, jointName = "torso_backleg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = 'torso_frontleg')
        pyrosim.Send_Motor_Neuron(name = 11, jointName="torso_leftleg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName="torso_rightleg")
        pyrosim.Send_Motor_Neuron(name = 13, jointName="frontleg_frontleg2")
        pyrosim.Send_Motor_Neuron(name = 14, jointName="backleg_backleg2")
        pyrosim.Send_Motor_Neuron(name = 15, jointName="leftleg_leftleg2")
        pyrosim.Send_Motor_Neuron(name = 16, jointName="rightleg_rightleg2")


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, 
                targetNeuronName=currentColumn + c.numSensorNeurons,
                weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        self.weights[random.randint(0, 2), random.randint(0, 1)] = random.random() * 2 - 1

    def Set_ID(self, id):
        self.myID = id

# import numpy as np 
# import os 
# import pyrosim.pyrosim as pyrosim
# import random
# import time
# import constants as c

# class SOLUTION: 
#     def __init__(self, nextAvailableID): 
#         self.weights = (np.random.rand(3, 2) *2 ) - 1
#         self.myID = nextAvailableID 
        
#     def Set_ID(self, id): 
#         self.myID = id

#     def Wait_For_Simulation_To_End(self): 
#         fitnessFileName = "fitness" + str(self.myID) + ".txt"
#         while not os.path.exists(fitnessFileName):
#             time.sleep(0.01)
#         file = open(fitnessFileName, "r")
#         self.fitness = float(file.read())
#         file.close()

#         os.system("rm " + fitnessFileName)

#     def Start_Simulation(self, directOrGUI): 
#         pyrosim.Start_SDF("world.sdf")
#         self.Create_World() 
#         self.Generate_Body() 
#         self.Generate_Brain() 
#         os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")

#     def Evaluate(self, directOrGUI):
#         pass
#         #file = open("fitness.txt", "r")
        

#     def Create_World(self): 
#         pyrosim.Send_Cube(name="Box", pos=[-1,-1,.5] , size=[1,1,1])
#         pyrosim.End() 
    
#     def Generate_Body(self): 
#         pyrosim.Start_URDF("body.urdf")
#         pyrosim.Send_Cube(name="torso", pos=[0, 0, 1] , size=[1,1,1])
#         pyrosim.Send_Joint(name = "torso_frontleg" , parent= "torso" , 
#         child = "frontleg" , type = "revolute", position = [0,0.5,1], jointAxis = "0 1 0")
#         pyrosim.Send_Cube(name="frontleg", pos=[0, 0.5, 0] , size=[.2,1,.2])
#         pyrosim.Send_Joint(name = "frontleg_frontleg2", parent = "frontleg", 
#         child = "frontleg2", type = "revolute", position = [0, 1, 0], jointAxis = "1 0 0")
#         pyrosim.Send_Cube(name = "frontleg2", pos = [0, 0, -0.5], size = [0.2, 1, .2])
#         pyrosim.Send_Joint(name = "torso_backleg" , parent= "torso" , child = "backleg" ,type = "revolute", position = [0, -0.5, 1], jointAxis = "0 1 0")
#         pyrosim.Send_Cube(name="backleg", pos=[0, -0.5, 0] , size=[.2 ,1,.2])
#         pyrosim.Send_Joint(name = "backleg_backleg2", parent = "backleg", child = "backleg2", 
#         type = "revolute", position = [0, -1, 0], jointAxis = "1 0 0")
#         pyrosim.Send_Cube(name = "backleg2", pos = [0, 0, -.5], size = [.2, .2, 1])

#         pyrosim.Send_Joint(name = "torso_leftleg", parent = "torso", child = "leftleg",
#         type = "revolute", position = [-0.5, 0, 1], jointAxis= "0 1 0")
#         pyrosim.Send_Cube(name="leftleg", pos=[-.5, 0, 0] , size=[1,.2,.2])

#         pyrosim.Send_Joint(name = "leftleg_leftleg2" , parent= "leftleg" , child = "leftleg2" ,
#          type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
#         pyrosim.Send_Cube(name="leftleg2", pos=[0, 0, -.5] , size=[.2,.2,1])

#         pyrosim.Send_Joint(name = "torso_rightleg" , parent= "torso" , child = "rightLeg" ,
#         type = "revolute", position = [0.5, 0, 1], jointAxis= "0 1 0")
#         pyrosim.Send_Cube(name="rightleg", pos=[.5, 0, 0] , size=[1,.2,.2])

#         pyrosim.Send_Joint(name = "rightleg_rightleg2" , parent= "rightleg" , child = "rightleg2" , 
#         type = "revolute", position = [1, 0,0], jointAxis="0 1 0")
#         pyrosim.Send_Cube(name="rightleg2", pos=[0, 0, -.5] , size=[.2,.2,1])

#         pyrosim.End()

#     def Generate_Brain(self): 
#         pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
#         pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
#         pyrosim.Send_Sensor_Neuron(name = 1, linkName = "backleg")
#         pyrosim.Send_Sensor_Neuron(name = 2, linkName = "frontleg")
#         pyrosim.Send_Sensor_Neuron(name = 3, linkName = "frontleg2")
#         pyrosim.Send_Sensor_Neuron(name = 4, linkName = "backleg2")
#         pyrosim.Send_Sensor_Neuron(name = 5, linkName = "leftleg")
#         pyrosim.Send_Sensor_Neuron(name = 6, linkName = "leftleg2")
#         pyrosim.Send_Sensor_Neuron(name = 7, linkName = "rightleg")
#         pyrosim.Send_Sensor_Neuron(name = 8, linkName = "rightleg2")

#         pyrosim.Send_Motor_Neuron(name = 9, jointName = "torso_backleg")
#         pyrosim.Send_Motor_Neuron(name = 10, jointName = "torso_frontleg")
#         pyrosim.Send_Motor_Neuron(name = 11, jointName = "torso_leftleg")
#         pyrosim.Send_Motor_Neuron(name = 12, jointName = "torso_rightleg")
#         pyrosim.Send_Motor_Neuron(name = 13, jointName = "frontleg_frontleg2")
#         pyrosim.Send_Motor_Neuron(name = 14, jointName = "backleg_backleg2")
#         pyrosim.Send_Motor_Neuron(name = 15, jointName = "leftleg_leftleg2")
#         pyrosim.Send_Motor_Neuron(name = 16, jointName = "rightleg_rightleg2")

#         for currentRow in range(c.numSensorNeurons): 
#             for currentColumn in range(c.numMotorNeurons):
#                 pyrosim.Send_Synapse( sourceNeuronName = currentRow , 
#                 targetNeuronName = currentColumn+ c.numSensorNeurons , 
#                 weight = self.weights[currentRow][currentColumn] )

#         pyrosim.End()

#     def Mutate(self): 
#         randomRow= random.randint(0,2)
#         randomCol = random.randint(0,1)
#         self.weights[randomRow, randomCol] = random.random() * 2 -1 
