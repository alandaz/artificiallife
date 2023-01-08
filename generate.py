import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

x = 0
for i in range(5): 
    y = 0 
    for j in range(5): 
        length = 1
        width = 1 
        height = 1
        z = 0.5 
        for k in range(0, 10): 
            pyrosim.Send_Cube(name = "Box", pos = [x, y, z], size = [length, width, height])
            z = z + height/2 + height * 0.9/2
            length = 0.9 * length 
            width = 0.9 * width 
            height = 0.9 * height 
        y += 1 
    x += 1 
pyrosim.End() 
