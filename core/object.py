from core import Vector


# Base class for scene objects and shapes
class Object:
    def __init__(self, pos):
        self.pos = pos
        self.max_offset = 0
        self.bounding_box = [Vector(0, 0, 0), Vector(0, 0, 0)]

    def __contains__(self, point):
        # Override in child class
        return False

    def bounds(self):
        return [corner + self.pos for corner in self.bounding_box]

    def compute_bounding_box(self, step):
        corner = self.pos - Vector(1, 1, 1) * self.max_offset
        size_steps = int(self.max_offset / step) * 2
        box = [self.pos.copy(), self.pos.copy()]

        for z in range(size_steps):
            for y in range(size_steps):
                for x in range(size_steps):
                    point = corner + Vector(x, y, z) * step
                    if point in self:
                        box[0].x = min(box[0].x, point.x)
                        box[0].y = min(box[0].y, point.y)
                        box[0].z = min(box[0].z, point.z)

                        box[1].x = max(box[1].x, point.x)
                        box[1].y = max(box[1].y, point.y)
                        box[1].z = max(box[1].z, point.z)

        # Increase bounds by 1 step in each direction and shift back to (0,0)
        box[0] += Vector(-1, -1, -1) * step - self.pos
        box[1] += Vector(1, 1, 1) * step - self.pos
        self.bounding_box = box

    def __str__(self):
        return f"Object at {self.pos}"

