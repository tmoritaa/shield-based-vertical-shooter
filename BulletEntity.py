from Box2D import *
from Entity import *
import TypeEnums

class BulletEntity(Entity):
    def __init__(self, id, health, damage, damageable, world, x, y, movePattern, attackPattern):
        super(BulletEntity, self).__init__(id, health, damage, damageable, 
                {},
                {},
                world, TypeEnums.TYPE_BULLET)
        self.body = None
        self.MovePattern = movePattern
        self.AttackPattern = attackPattern
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            bullet=True,
                            fixtures=b2FixtureDef(categoryBits=TypeEnums.CATEGORY_BULLET,
                                                  maskBits=TypeEnums.CATEGORY_PLAYER,
                                                  isSensor=True,
                                                  shape=b2CircleShape(radius=0.5), density=1)
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = True
        self.body.userData = self


    def move(self):
       self.MovePattern(self) 


    def attack(self):
        return self.AttackPattern(self)
