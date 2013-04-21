from CustomContactListener import *

class ContactInfo(object):
    def __init__(self, contactA, contactB):
        self.contactA = contactA
        self.contactB = contactB
        self.damageFrameCount = 0
        

class ContactManager(object):
    def __init__(self):
        self.DAMAGE_FRAME_COUNT_MOD = 20
        self._entityContactsDict = {}
        self.contactListener = CustomContactListener(self)


    def addContacts(self, contacts):
        dictKey = contacts[0].id + contacts[1].id
        self._entityContactsDict[dictKey] = ContactInfo(contacts[0], contacts[1])


    def removeContacts(self, contacts):
        dictKey = contacts[0].id + contacts[1].id
        del self._entityContactsDict[dictKey]


    def performContactAction(self):
        for contactsInfo in self._entityContactsDict.values():
            if contactsInfo.damageFrameCount == 0:
                if contactsInfo.contactA.damageable and contactsInfo.contactB.health > 0:
                    contactsInfo.contactA.health -= contactsInfo.contactB.damage
                
                if contactsInfo.contactB.damageable and contactsInfo.contactA.health > 0:
                    contactsInfo.contactB.health -= contactsInfo.contactA.damage

            contactsInfo.damageFrameCount += 1 
            contactsInfo.damageFrameCount %= self.DAMAGE_FRAME_COUNT_MOD


