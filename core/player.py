from time import sleep


SEPARATOR = "\n==FRAME==\n"


class Player(list):
    def __init__(self, filename, raw = False):
        self.filename = filename if raw else f"cache/{filename}.scn"
        self.read()

    def save(self):
        try:
            f = open(self.filename, "w")
            for frame in self:
                f.write(frame)
                f.write(SEPARATOR)
            f.close()
        finally:
            return self

    def read(self):
        try:
            f = open(self.filename, "r")
            self += f.read().split(SEPARATOR)
            f.close()
        finally:
            return self

    def frame(self, canvas):
        self.append(str(canvas))

    def play(self, fps = 60):
        index = 0
        while True:
            print(self[index % len(self)], flush=True)
            index += 1
            sleep(1 / fps)
            print("\n" * 100)

