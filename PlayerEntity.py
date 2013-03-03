import pygame
from Box2D import *
from Entity import *

class PlayerEntity(Entity):
    def __init__(self, world, x, y):
        super(PlayerEntity, self).__init__(world)
        self.body = None
        self.buttonDown = {"u" : -1, "d" : -1, "l" : -1, "r" : -1}
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            fixtures=b2FixtureDef(shape=b2CircleShape(radius=1), density=1)
                            )
        self.body.sleepingAllowed = False
        self.body.fixedRotation = True


    def _setPlayerVelocity(self, velx, vely):
        # assume player is in first index
        self.body.linearVelocity.x = velx
        self.body.linearVelocity.y = vely


    def _getPlayerVelocity(self):
        x = self.body.linearVelocity.x
        y = self.body.linearVelocity.y
        return (x, y)


    def handleInput(self, event):
            if event.type == pygame.KEYDOWN:
                curVel = self._getPlayerVelocity()
                setVelx = curVel[0]
                setVely = curVel[1]
                if event.key == pygame.K_w:
                    setVely = 5.0
                elif event.key == pygame.K_s:
                    setVely = -5.0
                if event.key == pygame.K_a:
                    setVelx = -5.0
                elif event.key == pygame.K_d:
                    setVelx = 5.0
                self._setPlayerVelocity(setVelx, setVely)

            if event.type == pygame.KEYUP:
                curVel = self._getPlayerVelocity()
                setVelx = curVel[0]
                setVely = curVel[1]
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    setVely = 0.0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    setVelx = 0.0
                self._setPlayerVelocity(setVelx, setVely)
