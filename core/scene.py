from core import Player


# Top-level class for the whole scene
class Scene:
    def __init__(self, name, camera, lights = [], objects = [], frame_count = 30):
        self.name = name
        self.player = Player(name)
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.frame_count = frame_count

    def render_frame(self, silent = False):
        self.camera.render(self.objects, self.lights)
        if not silent:
            print(self.camera.canvas)
        self.player.frame(self.camera.canvas)
        self.camera.canvas.clear()

    def post_frame_hook(self, index):
        print(f"Frame #{index}")

    def advance(self, index):
        for object in self.objects + self.lights + [self.camera]:
            if hasattr(object, "advance") and callable(object.advance):
                object.advance(object, index)

    def render(self, silent = False):
        for index in range(self.frame_count):
            self.render_frame(silent)
            self.post_frame_hook(index)
            self.advance(index)
        self.player.save()

    def start(self):
        if not self.player:
            self.render()
        self.player.play()

