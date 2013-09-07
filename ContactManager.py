from CustomContactListener import *

class ContactInfo(object):
    def __init__(self, contactA, contactB):
        self.contactA = contactA
        self.contactB = contactB
        self.dmgFrameCount = 0
        

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
        self._entityContactsDict[dictKey] = ContactInfo(contacts[0], 
                                                        contacts[1])


    def removeContacts(self, contacts):
        dictKey = self._createUniqueKey(contacts[0].id, contacts[1].id)
        del self._entityContactsDict[dictKey]


    def performContactAction(self):
        for contactsInfo in self._entityContactsDict.values():
            if contactsInfo.dmgFrameCount == 0:
                if contactsInfo.contactA.gameProps.dmgable and \
                   contactsInfo.contactB.gameProps.health > 0:
                    contactsInfo.contactA.gameProps.health -= \
                        contactsInfo.contactB.gameProps.dmg
                
                if contactsInfo.contactB.gameProps.dmgable and \
                   contactsInfo.contactA.gameProps.health > 0:
                    contactsInfo.contactB.gameProps.health -= \
                        contactsInfo.contactA.gameProps.dmg

            contactsInfo.dmgFrameCount += 1 
            contactsInfo.dmgFrameCount %= self.DAMAGE_FRAME_COUNT_MOD

