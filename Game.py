import pygame
import GraphicsManager
import EntityManager 

class Game(object):
    def __init__(self, _graphicsManager, _entityManager, _fps):
       self._graphicsManager = _graphicsManager 
       self._entityManager = _entityManager
       self._clock = pygame.time.Clock()
       self._running = True
       self.FPS = _fps
       self.TIMESTEP = 1.0 / self.FPS


    def start(self):
        while self._running:
            self._graphicsManager.drawEntities()
            self._entityManager.moveEntities()
            self._entityManager.attackEntities()
            self._handleInput()
            self._entityManager.destroyEntities()
            self._clock.tick(self.FPS) 


    def _handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self._running = False
                else:
                    self._entityManager.getPlayerEntity().handleInput(event)
            elif event.type == pygame.MOUSEMOTION:
               self._entityManager.getShieldEntity().handleInput(event) 


if __name__ == "__main__":
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    FPS = 60.0
    entityManager = EntityManager.EntityManager(FPS)
    graphicsManager = GraphicsManager.GraphicsManager(SCREEN_WIDTH, SCREEN_HEIGHT, entityManager)
    game = Game(graphicsManager, entityManager, FPS) 
    game.start()
