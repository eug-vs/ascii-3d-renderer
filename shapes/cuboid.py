class Cuboid:
    def __init__(self, center, size):
        self.center = center
        self.size = size

    def __contains__(self, point):
        diff = self.center - point
        fits_w = abs(diff[0]) < self.size[0] / 2
        fits_h = abs(diff[1]) < self.size[1] / 2
        fits_d = abs(diff[2]) < self.size[2] / 2
        return fits_w and fits_h and fits_d
