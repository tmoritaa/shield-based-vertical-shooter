from Box2D import *
import pygame
import TypeEnums

class GrManager(object):
    PIXELS_PER_METER = 20
    WIDTH = 0
    HEIGHT = 0


    @staticmethod
    def performScreenSpaceTransform(pos, transform):
        position = (transform * pos) * GrManager.PIXELS_PER_METER
        position = (int(round(position[0])), 
                    GrManager.HEIGHT - int(round(position[1])))
        return position


    def __init__(self, width, height, entityManager):
        pygame.init()
        GrManager.WIDTH = width
        GrManager.HEIGHT = height
        self._screen = pygame.display.set_mode((width, height), 0, 32)
        self._entityManager = entityManager

    
    def __del__(self):
        pygame.quit()


    def drawEntities(self):
        self._screen.fill((0, 0, 0, 0))

        for entity in self._entityManager.entityList:
            colour = (0, 0, 0, 255)
            if entity.grProps.grState == TypeEnums.GR_STATE_NORMAL:
                colour = (255, 255, 255, 255)
            elif entity.grProps.grState == TypeEnums.GR_STATE_DYING:
                colour = (255, 0, 0, 255)

            for fixture in entity.body.fixtures:
                shape = fixture.shape
                if isinstance(shape, b2CircleShape):
                    position = GrManager.performScreenSpaceTransform(
                        shape.pos, entity.body.transform)
                    radius = int(round(shape.radius * 
                                       GrManager.PIXELS_PER_METER))
                    pygame.draw.circle(self._screen, colour, position, radius)
                else:
                    vertices = [GrManager.performScreenSpaceTransform(
                                   v, 
                                   entity.body.transform) for v in shape.vertices
                               ]
                    pygame.draw.polygon(self._screen, colour, vertices)

        pygame.display.flip()

