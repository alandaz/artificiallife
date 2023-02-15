import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import decimal

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = numpy.random.rand(9, 8) * 2 - 1
        self.myID = nextAvailableID
        self.segments = random.randint(2, 5)
        self.sensornum = random.randint(1, self.segments)

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

    def Create_World(self):
        #pyrosim.Send_Cube(name="Box", pos=[0,0,3] , size=[.3,.3,.3])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        randomlinks = random.randint(3, 7)
  
        self.sensors = [random.randint(0, 1) for x in range(randomlinks)]
        print(self.sensors)


        for x in range(randomlinks):
            isSensor = False
            length = float(decimal.Decimal(random.randrange(50, 200))/100)
            width = float(decimal.Decimal(random.randrange(50, 200))/100)
            height = float(decimal.Decimal(random.randrange(50, 200))/100)

            if self.sensors[x] == 1:
                isSensor = True
            if self.sensors[x] == 0: 
                isSensor= False

            if x != 0:
                joint = 0 
                if x == 1: 
                    joint = min(pheight/2, height/2)
                else: 
                    joint = min(pheight/2, height/2) - pjoint
                pyrosim.Send_Joint(name = str(x - 1) + '_' + str(x) , parent= str(x-1) , child = str(x) , 
                type = "revolute", position = [0, previousWidth, joint], jointAxis="0 0 1")

            pheight = height
            previousWidth = width
            pjoint = 0 if x == 0 else pjoint + joint

            z = height/2 if x == 0 else -pjoint + height/2

            if isSensor == True: 
                pyrosim.Send_Cube(name=str(x), pos=[0, width / 2, z], size=[length, width, height], 
                color= "Green", code='    <color rgba="0 1.0 0.0 1.0"/>')
            if isSensor == False: 
                pyrosim.Send_Cube(name=str(x), pos=[0, width / 2, z], size=[length, width, height], 
                color= "Blue", code='    <color rgba="0 0.0 1.0 1.0"/>')

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        for x in range(len(self.sensors)):
            if(self.sensors[x] == 1):
                pyrosim.Send_Sensor_Neuron(name = x, linkName = str(x))
            if(x != len(self.sensors) - 1):
                pyrosim.Send_Motor_Neuron(name = x + len(self.sensors), jointName = str(x) + "_" + str(x+1))
     
        for x in range(len(self.sensors)):
            if(self.sensors[x] == 1):
                for y in range(len(self.sensors) - 1):
                    pyrosim.Send_Synapse(sourceNeuronName=x, targetNeuronName=y + self.sensornum, 
                    weight= self.weights[x][y])
        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons -1 )
        randomCol = random.randint(0, c.numMotorNeurons -1)
        self.weights[randomRow, randomCol] = (random.random() * 2 ) -1 

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID