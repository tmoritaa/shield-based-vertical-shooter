import pygame
import math
from Box2D import *
from Entity import *
import GraphicsManager

class ShieldEntity(Entity):
    def __init__(self, world, playerEntity):
        super( ShieldEntity, self ).__init__( world )
        self.SHIELD_RADIUS = 2
        self._playerEntity = playerEntity
        self._revJoint = None
        self._initBody( playerEntity.body.position[0], 
                        playerEntity.body.position[1] + self.SHIELD_RADIUS )


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=( x, y ), 
                            fixtures=b2FixtureDef( shape=b2PolygonShape( box=( 1.0, 0.25 ) ), density=1 )
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = False
        

    def setRevJoint(self, revJoint):
        self._revJoint = revJoint

    # currently assuming event is mouse motion, since only one being sent
    def handleInput(self, event):
        mousePos = event.pos
        playerBody = self._playerEntity.body
        tempPlayerPos = GraphicsManager.GraphicsManager.performScreenSpaceTransform( 
                    playerBody.position, playerBody.transform )

        playerPos = ( tempPlayerPos[0] / 2.0, ( tempPlayerPos[1] + GraphicsManager.GraphicsManager.HEIGHT ) / 2.0 )

        # performScreenSpaceTransform causes y to be inverted
        # invert it back
        dy = mousePos[1] - playerPos[1]
        dx = mousePos[0] - playerPos[0]

        rads = -math.atan2( dy, dx )  + 1.5 * math.pi

        rads %= 2 * math.pi

        jointAngle = self._revJoint.angle

        if jointAngle < 0:
            jointAngle %= -2 * math.pi
            jointAngle = 2 * math.pi + jointAngle
        else:
            jointAngle %= 2 * math.pi

        angleError = jointAngle - rads

        self._revJoint.motorSpeed = angleError * -1

