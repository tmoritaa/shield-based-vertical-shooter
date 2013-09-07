from Box2D import *
from Entity import *
import TypeEnums

class BulletEntity(Entity):
    def __init__(self, id, health, dmg, dmgable, world, x, y, 
                 movePattern, atkPattern):
        super(BulletEntity, self).__init__(id, health, dmg, dmgable, {}, {}, 
                                           world, TypeEnums.TYPE_BULLET)
        self.body = None
        self.MovePattern = movePattern
        self.AtkPattern = atkPattern
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            bullet=True,
                            fixtures=b2FixtureDef(
                                categoryBits=TypeEnums.CAT_BULLET,
                                maskBits=TypeEnums.CAT_PLAYER,
                                isSensor=True,
                                shape=b2CircleShape(radius=0.5), 
                                density=1)
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = True
        self.body.userData = self


    def move(self):
       self.MovePattern(self) 


    def atk(self):
        return self.AtkPattern(self)
