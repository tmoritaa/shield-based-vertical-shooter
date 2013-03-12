import pygame
import math
from Box2D import *
from Entity import *
import GraphicsManager

class ShieldEntity(Entity):
    def __init__(self, world, playerEntity):
        super( ShieldEntity, self ).__init__( world )
        self.SHIELD_RADIUS = 1.5
        self.SHIELD_RADIAL_VEL_MOD = 20
        self._playerEntity = playerEntity
        self._revJoint = None
        self._mouseAngle = 0 
        self._initBody( playerEntity.body.position[0], 
                        playerEntity.body.position[1] + self.SHIELD_RADIUS )


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=( x, y ), 
                            fixtures=b2FixtureDef( shape=b2PolygonShape( box=( 1.0, 0.25 ) ), density=0.5 )
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = False
        

    def move(self):
        jointAngle = self._revJoint.angle
        mouseAngle = self._mouseAngle

        jointAngle = self._revJoint.angle

        if jointAngle < 0:
            jointAngle %= -2 * math.pi
            jointAngle = 2 * math.pi + jointAngle
        else:
            jointAngle %= 2 * math.pi

        mouseAngle_alt = mouseAngle + 2.0 * math.pi
        jointAngle_alt = jointAngle + 2.0 * math.pi

        dist_temp1 = mouseAngle - jointAngle
        dist_temp2 = mouseAngle_alt - jointAngle
        dist_temp3 = mouseAngle - jointAngle_alt

        final_dist = dist_temp1 if abs(dist_temp1) < abs(dist_temp2) else dist_temp2
        final_dist = final_dist if abs(final_dist) < abs(dist_temp3) else dist_temp3

        self._revJoint.motorSpeed = final_dist * self.SHIELD_RADIAL_VEL_MOD 


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

        mouseAngle = -math.atan2( dy, dx )  + 1.5 * math.pi

        mouseAngle %= 2 * math.pi

        self._mouseAngle = mouseAngle

