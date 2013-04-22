import GraphicsDefines
import TypeEnums

class EntityGameProperties(object):
    def __init__(self, health, damage, damageable):
        self.health = health
        self.damage = damage
        self.damageable = damageable


# TODO: graphicState really isn't specific to graphics, but more like entity state in general
#       should move out
class EntityGraphicsProperties(object):
    def __init__(self, animDurations, animStateTransitions):
        # defaults
        self.currAnimDuration = 0 # also used to coordinate death timing
        self.graphicState = TypeEnums.GRAPHIC_STATE_NORMAL
        self.animDurations = {}
        self.animStateTransitions = {}
        self.animDurations[TypeEnums.GRAPHIC_STATE_DYING] = GraphicsDefines.GRAPHIC_DUR_DYING_DEFAULT 
        self.animStateTransitions[TypeEnums.GRAPHIC_STATE_DYING] = TypeEnums.GRAPHIC_STATE_DEAD 

        # if non default, set here
        for key in animDurations.keys():
            self.animDurations[key] = animDurations[key]

        for key in animStateTransitions.keys():
            self.animStateTransitions[key] = animStateTransitions[key]

    def getNextAnimState(self):
        return self.animStateTransitions[self.graphicState]

    def getCurrentAnimDuration(self):
        return self.animDurations[self.graphicState]

    def animDurationExists(self):
        if self.graphicState in self.animDurations:
            return True

        return False

    def stateTransitionExists(self):
        if self.graphicState in self.animStateTransitions:
            return True

        return False


class Entity(object):
    def __init__(self, id, health, damage, damageable, animDuration, animStateTransitions, world, type):
        self.id = id
        self.gameProperties     = EntityGameProperties(health, damage, damageable)
        self.graphicsProperties = EntityGraphicsProperties(animDuration, animStateTransitions)
        self.world = world
        self.type = type
        self.body = None

    def __del__(self):
        self.world.DestroyBody(self.body)

    # should be defined by every entity, but not yet being utilized properly
    def move(self):
        pass

    def setGraphicsState(self, graphicState):
        self.graphicsProperties.graphicState = graphicState
        self.graphicsProperties.animDuration = 0
