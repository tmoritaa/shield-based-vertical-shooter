from Box2D import *
import pygame

class GraphicsManager(object):
    PIXELS_PER_METER = 20
    WIDTH = 0
    HEIGHT = 0


    @staticmethod
    def performScreenSpaceTransform(pos, transform):
        position = ( transform * pos ) * GraphicsManager.PIXELS_PER_METER
        position = ( int( position[0] ), GraphicsManager.HEIGHT - int( position[1] ) )
        return position


    def __init__(self, width, height, entityManager):
        pygame.init()
        GraphicsManager.WIDTH = width
        GraphicsManager.HEIGHT = height
        self._screen = pygame.display.set_mode((width, height), 0, 32)
        self._entityManager = entityManager

    
    def __del__(self):
        pygame.quit()


    def drawEntities(self):
        self._screen.fill((0, 0, 0, 0))

        for entity in self._entityManager.entityList:
            for fixture in entity.body.fixtures:
                shape = fixture.shape
                if isinstance(shape, b2CircleShape):
                    position = GraphicsManager.performScreenSpaceTransform( shape.pos, entity.body.transform )
                    radius = int( shape.radius ) * GraphicsManager.PIXELS_PER_METER
                    pygame.draw.circle(self._screen, (255, 255, 255, 255), position, radius)
                else:
                    vertices = [GraphicsManager.performScreenSpaceTransform( v, entity.body.transform ) 
                                for v in shape.vertices]
                    pygame.draw.polygon(self._screen, (255, 255, 255, 255), vertices)

        pygame.display.flip()

