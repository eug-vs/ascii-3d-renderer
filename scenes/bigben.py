from math import pi as PI
from core import Vector, Canvas, Camera, Player, Scene
from shapes import Sphere, Cuboid

# Camera
canvas = Canvas(Vector(60, 30))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 3, 6)
focus = Vector(3, 3, 5)

def rotate(self):
    radius_vector = (camera.pos - focus).rotate_y(2 * PI / 60)
    camera.pos = focus + radius_vector
    camera.direction = radius_vector.normalized().reversed()

camera.advance = rotate


# Objects
body = Cuboid(Vector(3, 3, 5), Vector(1.2, 3, 1))
head = Sphere(Vector(3, 4.5, 5), 0.8)
balls = [Sphere(Vector(x, 1, 5), 1) for x in [2, 4]]
objects = [body, head] + balls


# Scene
scene = Scene("bigben", camera, objects)
scene.iterator = range(30)

