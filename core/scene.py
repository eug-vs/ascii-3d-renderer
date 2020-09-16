from core import Player


# Top-level class for the whole scene
class Scene(list):
    def __init__(self, name, camera, objects = [], iterator = []):
        self.name = name
        self.player = Player(name + ".scn")
        self.camera = camera
        self.objects = objects
        self.iterator = iterator

    def render_frame(self, silent = False):
        self.camera.render(self.objects)
        if not silent:
            print(self.camera.canvas)
        self.player.frame(self.camera.canvas)
        self.camera.canvas.clear()

    def post_frame_hook(self, iteration):
        print(f"Frame #{iteration}")

    def advance(self, iteration):
        for object in self.objects + [self.camera]:
            if hasattr(object, "advance") and callable(object.advance):
                object.advance(object, iteration)

    def render(self, silent = False):
        for iteration in self.iterator:
            self.render_frame(silent)
            self.post_frame_hook(iteration)
            self.advance(iteration)
        self.player.save(self.name + ".scn")

    def start(self):
        if not self.player:
            self.render()
        self.player.play()

