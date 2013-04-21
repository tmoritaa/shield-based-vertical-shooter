from Box2D import *
from EntityFactory import *

class EntityManager(object):
    def __init__(self, _fps, _contactListener):
        self.TIMESTEP = 1.0 / _fps 
        self.world = b2World(contactListener=_contactListener,
                                gravity=(0, 0), doSleep=False)
        self.entityList = [] # for now. Change to object list and change graphics manager to retrieve body from object
        self.playerEntity = None
        self.shieldEntity = None
        self.enemyEntityList = []
        self.bulletEntityList = []
        self._entityFactory = EntityFactory(self)
        self._initEntities()


    def moveEntities(self):
        for entity in self.entityList:
            entity.move()

        self.world.Step(self.TIMESTEP, 6, 2)
        self.world.ClearForces()


    def destroyEntities(self):
        destroyList = []
        for entity in self.entityList:
            if entity.health <= 0:
                destroyList.append(entity)

        for entity in destroyList:
            self.entityList.remove(entity)
            
            if entity.type == TypeEnums.TYPE_PLAYER:
                self.playerEntity = None
            elif entity.type == TypeEnums.TYPE_SHIELD:
                self.shieldEntity = None
            elif entity.type == TypeEnums.TYPE_BULLET:
                self.bulletEntityList.remove(entity)
            elif entity.type == TypeEnums.TYPE_ENEMY:
                self.enemyEntityList.remove(entity)

    def attackEntities(self):
        for entity in self.enemyEntityList:
            attackPatternList = entity.attack()
            for attack in attackPatternList:
                self._entityFactory.createAttackEntity( attack )


    # assumes player entity is in first index
    def getPlayerEntity(self):
        return self.playerEntity


    # assumes shield entity is in first index
    def getShieldEntity(self):
        return self.shieldEntity


    def _initEntities(self):
        playerX = 15
        playerY = 20

        self._entityFactory.createPlayerAndShieldEntity(playerX, playerY)
        self._entityFactory.createEnemyEntity(20, 20)
        
