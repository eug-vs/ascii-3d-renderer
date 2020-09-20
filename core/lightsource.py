class LightSource:
    def __init__(self, pos, brightness, ray_step):
        self.pos = pos
        self.brightness = brightness
        self.ray_step = ray_step

    def shoot_ray(self, direction, objects):
        point = self.pos
        ray = direction.normalized() * self.ray_step
        for step in range(int(self.brightness / self.ray_step)):
            point += ray
            for obj in objects:
                if point in obj:
                    return point
        return None

    def light(self, point, objects):
        direction = point - self.pos
        obstacle = self.shoot_ray(direction, objects)
        if obstacle:
            distance = (obstacle - self.pos).magnitude()
            if distance >= direction.magnitude():
                return distance
        return None

