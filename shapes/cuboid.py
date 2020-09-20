from core import Object

class Cuboid(Object):
    def __init__(self, pos, size):
        super().__init__(pos)
        self.size = size
        self.max_offset = max(size.x, size.y, size.z) / 2

    def __contains__(self, point):
        diff = self.pos - point
        fits_w = abs(diff[0]) < self.size[0] / 2
        fits_h = abs(diff[1]) < self.size[1] / 2
        fits_d = abs(diff[2]) < self.size[2] / 2
        return fits_w and fits_h and fits_d

    def __str__(self):
        return f"Cuboid of size {self.size} at {self.pos}"

