from core import Object


def intersect(interval, *intervals):
    '''Find an intersection of intervals'''
    if not intervals:
        return interval

    a, b = interval, intervals[0]
    if a[1] > b[0] and a[0] < b[1]:
        intermediate = max(a[0], b[0]), min(a[1], b[1])
        return intersect(intermediate, *intervals[1:])
    return None


# Base class for any ray emitter
class LightSource(Object):
    def __init__(self, pos, brightness, ray_step):
        super().__init__(pos)
        self.brightness = brightness
        self.ray_step = ray_step

    def light(self, point, objects):
        direction = point - self.pos
        obstacle = self.shoot_ray(direction, objects)
        if obstacle:
            distance = (obstacle - self.pos).magnitude()
            if distance >= direction.magnitude():
                return distance
        return None

    def shoot_ray(self, direction, objects):
        ray = direction.normalized() * self.ray_step

        step_count = int(self.brightness / self.ray_step)
        min_step = step_count
        collision_objects = []

        for object in objects:
            collision_step_intervals = []

            for axis in range(3):
                # For each axis find an interval where ray overlaps an object
                axis_collision_interval = sorted([
                    (corner[axis] - self.pos[axis]) / ray[axis] for corner in object.bounds()
                ])
                if all(bound < 0 for bound in axis_collision_interval):
                    # The ray will never hit an object
                    break
                collision_step_intervals.append(axis_collision_interval)
            else:
                intersection = intersect(*collision_step_intervals)
                if intersection:
                    # Intervals along each axis intersect => collision will occur
                    min_step = min(min_step, int(intersection[0]))
                    collision_objects.append(object)

        for step in range(min_step, step_count):
            point = self.pos + ray * step
            for object in collision_objects:
                if point in object:
                    return point
        return None

