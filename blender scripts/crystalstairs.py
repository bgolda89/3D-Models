import bpy
from bpy import context
from math import sin, cos, radians

cubeobject = bpy.ops.mesh.primitive_cube_add
cursor = context.scene.cursor_location

radialdist = 10.0

theta = 0.0
twopi_32 = 6.28/32


while theta < (4 * 6.28):
    x = cursor.x + theta * cos(theta)
    y = cursor.y + theta * sin(theta)
    z = cursor.z + theta * cos(theta)
    cubeobject(location=(x, y, z))
    bpy.ops.transform.resize(value = (0.4*theta, 0.1*theta, 0.075*theta))
    bpy.ops.object.modifier_add(type='SUBSURF')
    theta += twopi_32
