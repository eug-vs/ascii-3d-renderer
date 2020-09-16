class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __contains__(self, point):
        return (self.center - point).magnitude() < self.radius

