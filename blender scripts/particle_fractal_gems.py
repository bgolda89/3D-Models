import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 100.0
outsideradialdist = 20
theta = 0.0
outsidetheta = 0.0
twopi_32 = 6.28/32.0
twopi_16 = 6.28/16.0
twopi_8 = 6.28/8.0
z = 0
lastx = 1
lasty = 1
counter = 0

while outsidetheta < 6.28:
    xout = outsideradialdist * cos(outsidetheta) 
    yout = outsideradialdist * sin(outsidetheta)
    bpy.ops.transform.rotate(value = (theta))
    while theta < 6.28:
        radialdist = ((radialdist) * (counter))
        
        x = xout + (radialdist * cos(theta)) + (outsideradialdist * sin(theta))
        y = yout + (radialdist * sin(theta))  + (outsideradialdist * cos(theta))
        

        cubeobject(location=(x, y, z))
        bpy.ops.transform.resize(value = ((theta+1)/4, (theta+1)/2, (theta+1)/3))
        bpy.ops.transform.rotate(value = (outsidetheta))
        bpy.ops.object.modifier_add(type='SUBSURF')
        theta += twopi_16
        z += radialdist
        counter += 1
    outsidetheta += twopi_8
    z = 0
    counter = 0
    theta = 0
outsidetheta = 0

        
