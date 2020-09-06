from math import sqrt, cos, sin

# 3D vector
class Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)
        
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x, y, z)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Vector(x, y, z)

    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        return Vector(x, y, z)

    def __eq__(self, other):
        if other == 0:
            return self.x == 0 and self.y == 0 and self.z == 0
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, index):
        assert index < 3, "Error trying to access not-existent vector component"
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        return self.z

    def magnitude(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def normalized(self):
        return self / self.magnitude()

    def rotate_y(self, angle):
        x = self.x * cos(angle) + self.z * sin(angle)
        y = self.y
        z = self.z * cos(angle) - self.x * sin(angle)
        return Vector(x, y, z)

    def __str__(self):
        return f"[{round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)}]"


# Tests
if __name__ == "__main__":
    v = Vector(1, 2, 3)
    assert str(v) == "[1, 2, 3]"
    assert v + v == Vector(2, 4, 6)
    assert v * 2 == Vector(2, 4, 6)
    assert v - v == 0
    assert v / 2 == Vector(0.5, 1, 1.5)
    assert v - v / 2 == Vector(0.5, 1, 1.5)
    assert v[0] == 1 and v[1] == 2 and v[2] == 3
    assert Vector() == 0
    print("All tests have passed!")

