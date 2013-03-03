from Box2D import *
from PlayerEntity import *

class EntityManager(object):
    def __init__(self, _fps):
        self.TIMESTEP = 1.0 / _fps 
        self.world = b2World(gravity=(0, 0), doSleep=False)
        self.entityList = [] # for now. Change to object list and change graphics manager to retrieve body from object
        self._initEntities()


    def moveEntities(self):
        self.world.Step(self.TIMESTEP, 6, 2)


    def getPlayerEntity(self):
        return self.entityList[0]


    def _initEntities(self):
        playerX = 15
        playerY = 20

        playerEntity = PlayerEntity(self.world, playerX, playerY)

        #dynamicBody1 = self.world.CreateDynamicBody(
        #                    position=(playerX, playerY + 2), 
        #                    fixtures=b2FixtureDef(shape=b2PolygonShape(box=(2,0.1)), density=1)
        #                    )
        #dynamicBody1.sleepingAllowed = False
        #dynamicBody1.fixedRotation = True
        self.entityList.append(playerEntity)
        #self.entityList.append(self.world.CreateStaticBody(position=(0, 1), shapes=b2PolygonShape(box=(50, 5))))
