from math import pi as PI
from core import Vector, Canvas, Camera, Player, Scene
from shapes import Sphere, Cuboid

# Camera
canvas = Canvas(Vector(60, 30))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 3, 6)
camera_focus = Vector(3, 3, 5)
step_mag = 0.3

def rotate(self):
    camera.direction = (camera_focus - camera.pos).normalized()
    step = camera.direction.rotate_y(PI / 2).normalized() * step_mag
    camera.pos += step


# Objects
body = Cuboid(Vector(3, 3, 5), Vector(1.2, 3, 1))
head = Sphere(Vector(3, 4.5, 5), 0.8)
balls = [Sphere(Vector(x, 1, 5), 1) for x in [2, 4]]
objects = [body, head] + balls


# Scene
bigben = Scene("bigben", camera, objects)
bigben.post_frame_hook = rotate
bigben.iterator = range(int(2 * PI * (camera.pos - camera_focus).magnitude() / step_mag))

