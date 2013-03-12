class Entity(object):
    def __init__(self, world, type):
        self.world = world
        self.type = type
        self.body = None

    def __del__(self):
        self.world.DestroyBody(self.body)

    # should be defined by every entity, but not yet being utilized properly
    def move(self):
        pass
