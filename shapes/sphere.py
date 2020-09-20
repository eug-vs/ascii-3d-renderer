from core import Object

class Sphere(Object):
    def __init__(self, pos, radius):
        super().__init__(pos)
        self.radius = radius
        self.max_offset = radius

    def __contains__(self, point):
        return (self.pos - point).magnitude() < self.radius

    def __str__(self):
        return f"Sphere of radius {self.radius} at {self.pos}"
