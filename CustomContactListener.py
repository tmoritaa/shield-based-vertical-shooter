from Box2D import *
import TypeEnums

class CustomContactListener(b2ContactListener):
    def __init__(self, entityManager):
        b2ContactListener.__init__(self)
        self._entityManager = entityManager

    def BeginContact(self, contact):
        entityA = contact.fixtureA.body.userData
        entityB = contact.fixtureB.body.userData

        playerEntity = None
        bulletEntity = None
        shieldEntity = None
        enemyEntity = None

        if entityA.type == TypeEnums.TYPE_PLAYER:
            playerEntity = entityA
        elif entityA.type == TypeEnums.TYPE_SHIELD:
            shieldEntity = entityA
        elif entityA.type == TypeEnums.TYPE_BULLET:
            bulletEntity = entityA
        elif entityA.type == TypeEnums.TYPE_ENEMY:
            enemyEntity = entityA

        if entityB.type == TypeEnums.TYPE_PLAYER:
            playerEntity = entityB
        elif entityB.type == TypeEnums.TYPE_SHIELD:
            shieldEntity = entityB
        elif entityB.type == TypeEnums.TYPE_BULLET:
            bulletEntity = entityB
        elif entityB.type == TypeEnums.TYPE_ENEMY:
            enemyEntity = entityB

        if bulletEntity and shieldEntity:
            self._entityManager.destroyEntityList.append(bulletEntity)
            self._entityManager.bulletEntityList.remove(bulletEntity)
            self._entityManager.entityList.remove(bulletEntity)

        print "begin"

    def EndContact(self, contact):
        print "end"
        pass

    def PreSolve(self, contact, oldManifold):
        pass

    def PostSolve(self, contact, impulse):
        pass
