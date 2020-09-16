from math import cos, pi as PI


# Rotate an object around focus point
def rotate(focus, angle, change_direction = True):
    def advance(self, *args):
        radius_vector = (self.pos - focus).rotate_y(angle)
        self.pos = focus + radius_vector
        if change_direction:
            self.direction = radius_vector.normalized().reversed()
    return advance


# Oscillate object along direction
def oscillate(direction, magnitude, period):
    def advance(self, index):
        multiplier = cos(2 * PI * index / period)
        self.pos += direction.normalized() * magnitude * multiplier
    return advance


# Combine multiple dynamic motions
def combine(*methods):
    def advance(self, *args):
        for method in methods:
            method(self, *args)
    return advance

