from vector import Vector
from math import sqrt, tan, pi as PI


# Camera class for scene
class Camera:
    def __init__(self, pos, direction, canvas, angle, max_range, distance = 1):
        self.pos = pos
        self.direction = direction
        self.angle = angle
        self.distance = distance
        self.canvas = canvas
        self.ray_step = max_range / len(canvas.chars)
        self.max_range = max_range
        self.screen_width = distance * tan(angle / 2) * 2
        self.screen_height = self.screen_width / canvas.aspect_ratio()

    def screen(self):
        center = self.pos + (self.direction * self.distance)
        width = self.screen_width
        height = self.screen_height

        h_step = self.direction.rotate_y(PI / 2).normalized() * width / self.canvas.width()
        v_step = Vector(0, -1, 0) * height / self.canvas.height()

        corner = center - h_step * (self.canvas.width() / 2) - v_step * (self.canvas.height() / 2)

        return {
            "v_step": v_step,
            "h_step": h_step,
            "corner": corner,
        }

    def render(self, objects):
        screen = self.screen()

        ray_dir = screen["corner"] - self.pos
        for j in range(self.canvas.height()):
            ray_dir += screen["v_step"]
            for i in range(self.canvas.width()):
                ray_dir += screen["h_step"]

                ray = ray_dir.normalized() * self.ray_step

                point = self.pos
                for step in range(int(self.max_range / self.ray_step)):
                    point += ray
                    for obj in objects:
                        if point in obj:
                            dist = step * self.ray_step / self.max_range
                            self.canvas[j][i] = min(dist, self.canvas[j][i])
                            break
                    else:
                        continue
                    break

            ray_dir -= screen["h_step"] * self.canvas.width()


