from math import pi as PI
from vector import Vector
from canvas import Canvas
from camera import Camera
from sphere import Sphere


# Scene
canvas = Canvas(Vector(40, 20))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 2, 10)
sphere = Sphere(Vector(3, 3, 7), 1)


while(True):
    camera.capture(sphere)
    camera.direction = camera.direction.rotate_y( - PI / 360)
    print(canvas)
    canvas.clear()
    camera.pos += Vector(0.0, 0.0, 0.1)

