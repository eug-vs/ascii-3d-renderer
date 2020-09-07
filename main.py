from math import pi as PI
from vector import Vector
from canvas import Canvas
from camera import Camera
from sphere import Sphere
from cuboid import Cuboid


# Scene
canvas = Canvas(Vector(60, 30))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 2, 6)

# Objects
center = Vector(3, 3, 3)
cube = Cuboid(center, Vector(2, 2, 2))
sphere = Sphere(center, 1)
objects = [cube]


camera_focus = Vector(3, 3, 3)
step_mag = 0.1

while(True):
    camera.render(objects)
    camera.direction = (camera_focus - camera.pos).normalized()
    step = camera.direction.rotate_y(PI / 2).normalized() * step_mag
    print(canvas)
    canvas.clear()
    camera.pos += step

