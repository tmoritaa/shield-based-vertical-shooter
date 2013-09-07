from Box2D import *
from PlayerEntity import *
from ShieldEntity import *
from EnemyEntity import *
from BulletEntity import *
import EnemyEntityMovePatterns
import EnemyEntityAtkPatterns

class EntityFactory(object):
    def __init__(self, entityManager):
        self._entityManager = entityManager
        self.world = self._entityManager.world
        self._entityId = 0

    def createPlayerAndShieldEntity(self, playerX, playerY):
        self._entityId += 1
        playerEntity = PlayerEntity(self._entityId, 1, 0, True, 
                                    self.world, playerX, playerY)

        self._entityId += 1
        shieldEntity = ShieldEntity(self._entityId, 1, 1, False, 
                                    self.world, playerEntity)

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
        self._entityId += 1
        enemyEntity = EnemyEntity(self._entityId, 3, 1, True, 
                                  self.world, posX, posY, 
                                  EnemyEntityMovePatterns.MovePatternBasic,
                                  EnemyEntityAtkPatterns.AtkPatternBasic)

        self._entityManager.entityList.append(enemyEntity)
        self._entityManager.enemyEntityList.append(enemyEntity)


    def createAtkEntity(self, atkPropList):
        bulletEntityList = []
        self._entityId += 1
        if atkPropList[0] == TypeEnums.BULLET_NORMAL:
            bulletEntity0 = BulletEntity(
                                self._entityId, 1, 1, True, 
                                self.world, 
                                atkPropList[1][0], 
                                atkPropList[1][1],
                                atkPropList[2], 
                                atkPropList[3])
            bulletEntityList.append(bulletEntity0)

        for bullet in bulletEntityList:
            self._entityManager.entityList.append(bullet)
            self._entityManager.bulletEntityList.append(bullet)
        
