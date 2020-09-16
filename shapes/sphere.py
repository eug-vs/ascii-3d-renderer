class Sphere:
    def __init__(self, pos, radius):
        self.pos = pos
        self.radius = radius

    def __contains__(self, point):
        return (self.pos - point).magnitude() < self.radius

