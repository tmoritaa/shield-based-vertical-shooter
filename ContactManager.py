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


    # creates unique key from two integers, and uses that as key
    # concept using Cantor Pairing functions as described at:
    # www.stackoverflow.com/questions/919612/mapping-two-integers-to-one-in-a-unique-and-deterministic-way
    def _createUniqueKey(self, _num1, _num2):
        ls = [_num1, _num2]
        for i in range(len(ls)):
            val = ls[i]
            if val >= 0:
                ls[i] = val * 2
            else:
                ls[i] = -val * 2 - 1

        dictKey = 0.5 * (ls[0] + ls[1]) * (ls[0] + ls[1] + 1) + ls[1] 
        
        return dictKey


    def addContacts(self, contacts):
        dictKey = self._createUniqueKey(contacts[0].id, contacts[1].id)
        self._entityContactsDict[dictKey] = ContactInfo(contacts[0], contacts[1])


    def removeContacts(self, contacts):
        dictKey = self._createUniqueKey(contacts[0].id, contacts[1].id)
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


