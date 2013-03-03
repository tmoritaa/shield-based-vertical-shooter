from Box2D import *
import pygame

class GraphicsManager(object):
    def __init__(self, width, height, entityManager):
        pygame.init()
        self.width = width
        self.height = height
        self._screen = pygame.display.set_mode((width, height), 0, 32)
        self._entityManager = entityManager
        self.PIXELS_PER_METER = 20

    
    def __del__(self):
        pygame.quit()


    def drawEntities(self):
        self._screen.fill((0, 0, 0, 0))

        for entity in self._entityManager.entityList:
            for fixture in entity.body.fixtures:
                shape = fixture.shape
                if isinstance(shape, b2CircleShape):
                    position = (entity.body.transform * shape.pos) * self.PIXELS_PER_METER
                    position = (int(position.x), self.height - int(position.y))
                    radius = int(shape.radius) * self.PIXELS_PER_METER
                    pygame.draw.circle(self._screen, (255, 255, 255, 255), position, radius)
                else:
                    vertices = [(entity.body.transform*v)*self.PIXELS_PER_METER for v in shape.vertices]
                    vertices = [(v[0], self.height - v[1]) for v in vertices]
                    pygame.draw.polygon(self._screen, (255, 255, 255, 255), vertices)

        pygame.display.flip()

