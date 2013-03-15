from Box2D import *
import TypeEnums

class CustomContactListener(b2ContactListener):
    def __init__(self, entityManager):
        b2ContactListener.__init__(self)
        self._entityManager = entityManager

    def BeginContact(self, contact):
        #entityList = []
        #entityA = contact.fixtureA.body.userData
        #entityB = contact.fixtureB.body.userData

        #if entityA.type == TypeEnums.TYPE_ENEMY and entityB.type == TypeEnums.TYPE_SHIELD:
            #self._entityManager.destoryEntityList.append(entityA)
            #self._entityManager.enemyEntityList.remove(entityA)
            #self._entityManager.entityList.remove(entityA)
        #elif entityA.type == TypeEnums.TYPE_SHIELD and entityB.type == TypeEnums.TYPE_ENEMY:
            #self._entityManager.destoryEntityList.append(entityB)
            #self._entityManager.enemyEntityList.remove(entityB)
            #self._entityManager.entityList.remove(entityB)
        print "begin"

    def EndContact(self, contact):
        print "end"
        pass

    def PreSolve(self, contact, oldManifold):
        print "presolve"
        pass

    def PostSolve(self, contact, impulse):
        print "postsolve"
        pass
