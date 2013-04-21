from Box2D import *
import TypeEnums

class CustomContactListener(b2ContactListener):
    def __init__(self, contactManager):
        b2ContactListener.__init__(self)
        self._contactManager = contactManager 

    def BeginContact(self, contact):
        entityA = contact.fixtureA.body.userData
        entityB = contact.fixtureB.body.userData

        self._contactManager.addContacts((entityA, entityB))

        print "begin"

    def EndContact(self, contact):
        entityA = contact.fixtureA.body.userData
        entityB = contact.fixtureB.body.userData

        self._contactManager.removeContacts((entityA, entityB))
        print "end"
        pass

    def PreSolve(self, contact, oldManifold):
        pass

    def PostSolve(self, contact, impulse):
        pass
