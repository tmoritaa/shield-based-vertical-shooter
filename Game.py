import pygame
import GrManager
import EntityManager 
import ContactManager

class Game(object):
    def __init__(self, _grManager, _entityManager, _contactManager, _fps):
       self._grManager = _grManager 
       self._entityManager = _entityManager
       self._contactManager = _contactManager
       self._clock = pygame.time.Clock()
       self._running = True
       self.FPS = _fps
       self.TIMESTEP = 1.0 / self.FPS


    def start(self):
        while self._running:
            self._grManager.drawEntities()
            self._entityManager.moveEntities()
            self._entityManager.atkEntities()
            self._contactManager.performContactAction()
            self._entityManager.stateTransitionEntities()
            self._entityManager.destroyEntities()
            self._handleInput()
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
    contactManager = ContactManager.ContactManager()
    entityManager = EntityManager.EntityManager(FPS, 
                                                contactManager.contactListener)
    grManager = GrManager.GrManager(SCREEN_WIDTH, SCREEN_HEIGHT, entityManager)
    game = Game(grManager, entityManager, contactManager, FPS) 
    game.start()
