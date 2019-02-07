import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 75.0
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
        radialdist = (radialdist * theta * counter)
        
        x = (theta * xout) - (radialdist * cos(theta)) 
        y = (theta * yout) - (radialdist * sin(theta))
        
        z = xout * sin(theta) + (radialdist * cos(theta))
        
        cubeobject(location=(x, y, z))
        bpy.ops.transform.resize(value = (theta * theta, theta * theta, theta * theta))
        bpy.ops.transform.rotate(value = (theta))
        bpy.ops.object.modifier_add(type='SUBSURF')
        theta += twopi_16
        counter += 10
    outsidetheta += twopi_8
    z = 0
    counter = 0
    theta = 0
outsidetheta = 0

        
