from Box2D import *
from EntityFactory import *
import TypeEnums

class EntityManager(object):
    def __init__(self, _fps, _contactListener):
        self.TIMESTEP = 1.0 / _fps 
        self.world = b2World(contactListener=_contactListener,
                             gravity=(0, 0), doSleep=False)
        self.entityList = [] # for now. Change to object list and change gr manager to retrieve body from object
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


    # TODO: currently even if entities are destroyed here,
    # if they are still in contact with another entity and 
    # the ContactManager still includes them in it's dict,
    # the entity being destroyed here will not actually be
    # destroyed until the contact is ended. Should be fixed
    def destroyEntity(self, entity):
        self.entityList.remove(entity)
        
        if entity.type == TypeEnums.TYPE_PLAYER:
            self.playerEntity = None
        elif entity.type == TypeEnums.TYPE_SHIELD:
            self.shieldEntity = None
        elif entity.type == TypeEnums.TYPE_BULLET:
            self.bulletEntityList.remove(entity)
        elif entity.type == TypeEnums.TYPE_ENEMY:
            self.enemyEntityList.remove(entity)


    def destroyEntities(self):
        destroyEntityList = []
        for entity in self.entityList:
            if entity.grProps.grState == TypeEnums.GR_STATE_DEAD:
                destroyEntityList.append(entity)

        for entity in destroyEntityList:
            self.destroyEntity(entity)


    def stateTransitionEntities(self):
        for entity in self.entityList:
            if entity.gameProps.health <= 0 and \
                    (entity.grProps.grState != TypeEnums.GR_STATE_DYING and \
                    entity.grProps.grState != TypeEnums.GR_STATE_DEAD):
                entity.setGrState(TypeEnums.GR_STATE_DYING)

            if entity.grProps.stateTransitionExists():
                totalAnimDur = 0
                if entity.grProps.animDurationExists():
                    totalAnimDur = entity.grProps.getCurrentAnimDuration()
                
                if entity.grProps.currAnimDuration >= totalAnimDur:
                    entity.setGrState(entity.grProps.getNextAnimState())

            entity.grProps.currAnimDuration += 1


    def atkEntities(self):
        for entity in self.enemyEntityList:
            atkPatternList = entity.atk()
            for atk in atkPatternList:
                self._entityFactory.createAtkEntity( atk )


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
        
