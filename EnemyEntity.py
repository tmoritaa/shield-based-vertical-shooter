from Box2D import *
from Entity import *
import TypeEnums

class EnemyEntity(Entity):
    def __init__(self, world, x, y, health, movePattern, attackPattern):
        super(EnemyEntity, self).__init__(world, TypeEnums.TYPE_ENEMY)
        self.body = None
        self.health = health
        self.MovePattern = movePattern
        self.AttackPattern = attackPattern
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            fixtures=b2FixtureDef(categoryBits=TypeEnums.CATEGORY_ENEMY,
                                                  maskBits=TypeEnums.CATEGORY_PLAYER,
                                                  isSensor=True,
                                                  shape=b2CircleShape(radius=1), density=1)
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = True
        self.body.userData = self


    def move(self):
       self.MovePattern(self) 


    def attack(self):
        return self.AttackPattern(self)
