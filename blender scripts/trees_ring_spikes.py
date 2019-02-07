import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 10.0
outsideradialdist = 100
theta = 0.0
outsidetheta = 0.0
twopi_32 = 6.28/32.0
twopi_16 = 6.28/16.0
twopi_8 = 6.28/8.0
z = 0

while outsidetheta < 6.28:
    xout = outsideradialdist * cos(outsidetheta) - outsidetheta
    yout = outsideradialdist * sin(outsidetheta) - outsidetheta
    while theta < 6.28:
        radialdist = radialdist * theta
        x = xout + radialdist * cos(theta)
        y = yout + radialdist * sin(theta)


        cubeobject(location=(x, y, z))
        bpy.ops.transform.resize(value = (theta+1, theta+1, theta+1))
        bpy.ops.transform.rotate(value = (outsidetheta))
        bpy.ops.object.modifier_add(type='SUBSURF')
        theta += twopi_16
        z += 5
    outsidetheta += twopi_8
    z = 0
    theta = 0
outsidetheta = 0

        
