# Rotate an object around focus point
def rotate(focus, angle, change_direction = True):
    def advance(self, iteration):
        radius_vector = (self.pos - focus).rotate_y(angle)
        self.pos = focus + radius_vector
        if change_direction:
            self.direction = radius_vector.normalized().reversed()
    return advance

