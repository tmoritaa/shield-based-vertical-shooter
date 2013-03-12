from Box2D import *
from PlayerEntity import *
from ShieldEntity import *
from EnemyEntity import *

class EntityFactory(object):
    def __init__(self, entityManager):
        self._entityManager = entityManager
        self.world = self._entityManager.world

    def createPlayerAndShieldEntity(self, playerX, playerY):
        playerEntity = PlayerEntity(self.world, playerX, playerY)

        shieldEntity = ShieldEntity(self.world, playerEntity)

        revJointDef = b2RevoluteJointDef(
                            bodyA = playerEntity.body,
                            bodyB = shieldEntity.body,
                            anchor = playerEntity.body.worldCenter,
                            enableMotor = True,
                            maxMotorTorque = 1000,
                            motorSpeed = 0)

        joint = self.world.CreateJoint(revJointDef)

        shieldEntity.setRevJoint(joint)

        self._entityManager.entityList.append(playerEntity)
        self._entityManager.entityList.append(shieldEntity)
        self._entityManager.playerEntity = playerEntity
        self._entityManager.shieldEntity = shieldEntity


    # later add string for specifying enemy type
    def createEnemyEntity(self, posX, posY):
        enemyEntity = EnemyEntity(self.world, posX, posY)

        self._entityManager.entityList.append(enemyEntity)
        self._entityManager.enemyEntityList.append(enemyEntity)
