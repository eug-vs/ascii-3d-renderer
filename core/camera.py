from math import sqrt, tan, pi as PI
from core import Vector, LightSource


# Camera class for scene
class Camera(LightSource):
    def __init__(self, pos, direction, canvas, angle, max_range, distance = 1):
        super().__init__(pos, max_range, max_range / len(canvas.chars))
        self.direction = direction
        self.angle = angle
        self.distance = distance
        self.canvas = canvas
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

    def render(self, objects, lights = []):
        screen = self.screen()

        ray_dir = screen["corner"] - self.pos
        for j in range(self.canvas.height()):
            ray_dir += screen["v_step"]
            for i in range(self.canvas.width()):
                ray_dir += screen["h_step"]

                point = self.shoot_ray(ray_dir, objects)
                if point:
                    dist = (point - self.pos).magnitude()
                    if lights:
                        dist = None
                        for source in lights:
                            new_dist = source.light(point, objects)
                            if dist and new_dist:
                                dist = min(dist, new_dist)
                            elif new_dist:
                                dist = new_dist
                    if dist:
                        self.canvas[j][i] = dist / self.brightness
                    else:
                        self.canvas[j][i] = 0.99

            ray_dir -= screen["h_step"] * self.canvas.width()

