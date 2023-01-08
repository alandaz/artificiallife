
import pyrosim.pyrosim as pyrosim

x= 0
y = 0 
z = 0.5

length = 1
height = 1 
width = 1 

def Create_World(): 
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name = "Box", pos = [x, y, z], size = [length, width, height])
    pyrosim.End() 

def Create_Robot(): 
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name = "Torso", pos = [x, y, z], size = [length, width, height])
    pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [1, 0, 1.5])
    pyrosim.Send_Cube(name = "Leg", pos = [x, y, z], size = [length, width, height])
    
    pyrosim.End() 


Create_World() 
Create_Robot() 