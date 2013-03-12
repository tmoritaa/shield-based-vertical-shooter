from Box2D import *
from Entity import *

class EnemyEntity(Entity):
    def __init__(self, world, x, y):
        super(EnemyEntity, self).__init__(world)
        self.body = None
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            fixtures=b2FixtureDef(shape=b2CircleShape(radius=1), density=1)
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = True
