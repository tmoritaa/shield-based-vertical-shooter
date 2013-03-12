import pygame
from Box2D import *
from Entity import *

class PlayerEntity(Entity):
    def __init__(self, world, x, y):
        super(PlayerEntity, self).__init__(world)
        self.body = None
        self.buttonDownOrder = {"u" : -1, "d" : -1, "l" : -1, "r" : -1}
        self.keyDownCount = 0
        self._initBody(x, y)


    def _initBody(self, x, y):
        self.body = self.world.CreateDynamicBody(
                            position=(x, y), 
                            fixtures=b2FixtureDef(shape=b2CircleShape(radius=1), density=100)
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


    def _determineAndSetPlayerVelocity(self):
        velX = 0
        velY = 0
        upVal = self.buttonDownOrder['u']
        downVal = self.buttonDownOrder['d']
        leftVal = self.buttonDownOrder['l']
        rightVal = self.buttonDownOrder['r']

        if (upVal == 0 or upVal == 1):
            velY = 5
        elif (downVal == 0 or downVal == 1):
            velY = -5
        if (leftVal == 0 or leftVal == 1):
            velX = -5
        elif (rightVal == 0 or rightVal == 1):
            velX = 5

        self._setPlayerVelocity(velX, velY)


    def move(self):
        self._determineAndSetPlayerVelocity()


    def handleInput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.buttonDownOrder['u'] = self.keyDownCount
            elif event.key == pygame.K_s:
                self.buttonDownOrder['d'] = self.keyDownCount
            if event.key == pygame.K_a:
                self.buttonDownOrder['l'] = self.keyDownCount
            elif event.key == pygame.K_d:
                self.buttonDownOrder['r'] = self.keyDownCount

            self.keyDownCount += 1

        if event.type == pygame.KEYUP:
            cancelCount = 0
            if event.key == pygame.K_w:
                cancelCount = self.buttonDownOrder['u']
                self.buttonDownOrder['u'] = -1
            elif event.key == pygame.K_s:
                cancelCount = self.buttonDownOrder['d']
                self.buttonDownOrder['d'] = -1 
            if event.key == pygame.K_a:
                cancelCount = self.buttonDownOrder['l']
                self.buttonDownOrder['l'] = -1
            elif event.key == pygame.K_d:
                cancelCount = self.buttonDownOrder['r']
                self.buttonDownOrder['r'] = -1

            self.keyDownCount -= 1

            for item in self.buttonDownOrder.items():
                if item[1] > cancelCount:
                    self.buttonDownOrder[item[0]] -= 1

