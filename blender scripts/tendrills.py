import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 10.0
outsideradialdist = 40
theta = 0.0
outsidetheta = 0.0
twopi_32 = 6.28/32
twopi_16 = 6.28/16
z = 1

while outsidetheta < 6.28:
    xout = outsideradialdist * cos(outsidetheta)
    yout = outsideradialdist * sin(outsidetheta)
    while theta < (1 * 6.28):
        x = xout + radialdist * cos(theta)
        y = yout + radialdist * sin(theta)
        

        cubeobject(location=(x, y, z))
        bpy.ops.transform.resize(value = (theta, theta, theta))
        bpy.ops.transform.rotate(value = (theta))
        bpy.ops.object.modifier_add(type='SUBSURF')
        theta += twopi_32
        z += 3
    outsidetheta += twopi_16
    z = 0
    
    theta = 0
outsidetheta = 0

        
