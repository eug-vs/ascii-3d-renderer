from vector import Vector
from math import sqrt, tan, pi as PI


# Camera class for scene
class Camera:
    def __init__(self, pos, direction, canvas, angle, max_range, ray_step = 0.1, distance = 1):
        self.pos = pos
        self.direction = direction
        self.angle = angle
        self.distance = distance
        self.canvas = canvas
        self.ray_step = ray_step
        self.max_range = max_range

    def screen(self):
        center = self.pos + (self.direction * self.distance)

        width = self.distance * tan(self.angle / 2) * 2
        height = width / self.canvas.aspect_ratio()

        h_step = self.direction.rotate_y(PI / 2).normalized() * width / self.canvas.width()
        v_step = Vector(0, -1, 0) * height / self.canvas.height()

        corner = center - h_step * (self.canvas.width() / 2) - v_step * (self.canvas.height() / 2)

        return {
            "center": center,
            "width": width,
            "height": height,
            "v_step": v_step,
            "h_step": h_step,
            "corner": corner,
        }

    def capture(self, obj):
        screen = self.screen()

        for j in range(self.canvas.height()):
            for i in range(self.canvas.width()):
                ray_screen_pos = screen["corner"] + screen["h_step"] * i + screen["v_step"] * j
                ray = (ray_screen_pos - self.pos).normalized() * self.ray_step

                for step in range(int(self.max_range / self.ray_step)):
                    point = self.pos + ray * step
                    if (point in obj):
                        self.canvas[j][i] = step * self.ray_step / self.max_range
                        break

