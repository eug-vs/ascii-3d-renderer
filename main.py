from math import pi as PI
from vector import Vector
from canvas import Canvas
from camera import Camera
from sphere import Sphere
from cuboid import Cuboid
from player import Player

NAME = "scene"

# TODO: create camera movement presets, like flying around the scene
# TODO: build BVH for objects for better performance in ray tracing

# Scene
canvas = Canvas(Vector(60, 30))
camera = Camera(Vector(3, 3, 0), Vector(0, 0, 1), canvas, PI / 3, 6)
camera_focus = Vector(3, 3, 5)
step_mag = 0.5

# Objects
body = Cuboid(Vector(3, 3, 5), Vector(1.2, 3, 1))
head = Sphere(Vector(3, 4.5, 5), 0.8)
balls = [Sphere(Vector(x, 1, 5), 1) for x in [2, 4]]
objects = [body, head] + balls


player = Player(NAME)
if not player:
    for i in range(int(2 * PI * (camera.pos - camera_focus).magnitude() / step_mag)):
        # Render
        camera.render(objects)
        print(canvas)
        player.frame(canvas)
        canvas.clear()

        # Rotate camera
        camera.direction = (camera_focus - camera.pos).normalized()
        step = camera.direction.rotate_y(PI / 2).normalized() * step_mag
        camera.pos += step

    player.save(NAME)

player.play()

