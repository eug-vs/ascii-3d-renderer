from core import Vector


FONT_ASPECT_RATIO = 1 / 2
CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


# Canvas for rendering
class Canvas:
    def __init__(self, size):
        self.size = size
        self.canvas = [[1 for i in range(self.width())] for j in range(self.height())]
        self.chars = CHARS

    def __getitem__(self, index):
        return self.canvas[index]

    def width(self):
        return self.size[0]

    def height(self):
        return self.size[1]

    def aspect_ratio(self):
        return FONT_ASPECT_RATIO * self.width() / self.height()

    def __str__(self):
        rows = ["".join([self.chars[int(dist * (len(self.chars) - 1))] for dist in row]) for row in self]
        return "\n".join(rows)

    def clear(self):
        for row in self:
            for i in range(len(row)):
                row[i] = 1


# Tests
if __name__ == "__main__":
    size = Vector(40, 20)
    c = Canvas(size)
    assert c.width() == 40
    assert c.height() == 20
    assert len(str(c)) == (40 + 1) * 20 - 1
    assert c.aspect_ratio() == 1
    assert c[0][0] == 1
    print("All tests have passed!")

