import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 10.0

theta = 0.0
twopi_32 = 6.28/32


while theta < (1 * 6.28):
    x = cursor.x + theta * sin(theta)
    y = cursor.y + theta * cos(theta)
    z = cursor.z * sin(theta)
    cubeobject(location=(x, y, z))
    bpy.ops.transform.resize(value = (theta/0.3, theta/2, 0.075*theta))
    bpy.ops.transform.rotate(value = (2 * theta))
    bpy.ops.object.modifier_add(type='SUBSURF')
    theta += twopi_32
