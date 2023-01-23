import pyrosim.pyrosim as pyrosim


def Create_World(): 
    pyrosim.Send_Cube(name="Box", pos=[-1,-1,.5] , size=[1,1,1])
    pyrosim.End() 

#def Create_Robot(): 
    
def Generate_Body(): 
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5] , size=[1,1,1])
    pyrosim.Send_Joint(name = "torso_frontleg" , parent= "torso" , child = "frontleg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="frontleg", pos=[-0.5, 0, -0.5] , size=[1,1,1])
    pyrosim.Send_Joint(name = "torso_backleg" , parent= "torso" , child = "backleg" , type = "revolute", position = [2, 0, 1])
    pyrosim.Send_Cube(name="backleg", pos=[0.5, 0, -.5] , size=[1 ,1,1])
    pyrosim.End()

def Generate_Brain(): 
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "torso")
    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "backleg")
    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "frontleg")
    pyrosim.Send_Motor_Neuron(name = 3, jointName = "torso_backleg")
    pyrosim.Send_Motor_Neuron(name = 4, jointName = "torso_frontleg")
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight =-1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -1.0 )
    pyrosim.Send_Synapse( sourceNeuronName = 1, targetNeuronName = 4 , weight = -1.0 )
    pyrosim.End()

Generate_Body()
Generate_Brain()

pyrosim.Start_SDF("world.sdf")
Create_World() 
#Create_Robot() 