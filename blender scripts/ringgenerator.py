import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 10.0

theta = 0.0
twopi_32 = 6.28/32

while theta < 6.28:
    x = cursor.x + radialdist * cos(theta)
    y = cursor.y + radialdist * sin(theta)
    z = cursor.z
    cubeobject(location=(x, y, z))
    bpy.ops.object.modifier_add(type='SUBSURF')
    theta += twopi_32
    


