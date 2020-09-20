from math import pi as PI
from core import Vector, Canvas, Camera, Scene, LightSource
from core.dynamics import rotate, oscillate, combine
from shapes import Sphere, Cuboid

# Camera
canvas = Canvas(Vector(60, 30))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 3, 13)
camera.advance = combine(
    rotate(Vector(3, 3, 5), -2 * PI / 60),
)

main_light = LightSource(Vector(2, 4.5, 1), 9, 9 / len(canvas.chars))
secondary_light = LightSource(Vector(6, 3, 7), 4, 4 / len(canvas.chars))
lights = [main_light, secondary_light]


# Objects
body = Cuboid(Vector(3, 3, 5), Vector(1.2, 3, 1))
head = Sphere(Vector(3, 4.5, 5), 0.8)
balls = [Sphere(Vector(x, 1, 5), 1) for x in [2, 4]]
wall = Cuboid(Vector(3, 3, 11), Vector(10, 10, 1))
corner = Cuboid(Vector(-3, 3, 5), Vector(1, 10, 10))
floor = Cuboid(Vector(3, 0, 5), Vector(10, 1, 10))
objects = [body, head, wall, corner, floor] + balls

# Scene
scene = Scene("bigben", camera, lights, objects, frame_count=60)

