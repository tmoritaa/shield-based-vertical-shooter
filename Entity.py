import GrDefines
import TypeEnums

class EntityGameProps(object):
    def __init__(self, health, dmg, dmgable):
        self.health = health
        self.dmg = dmg
        self.dmgable = dmgable


# TODO: grState really isn't specific to gr, but more like entity state in general
#       should move out
class EntityGrProps(object):
    def __init__(self, animDurations, animStateTransitions):
        # defaults
        self.currAnimDuration = 0 # also used to coordinate death timing
        self.grState = TypeEnums.GR_STATE_NORMAL
        self.animDurations = {}
        self.animStateTransitions = {}
        self.animDurations[TypeEnums.GR_STATE_DYING] = \
            GrDefines.GR_DUR_DYING_DEFAULT 
        self.animStateTransitions[TypeEnums.GR_STATE_DYING] = \
            TypeEnums.GR_STATE_DEAD 

        # if non default, set here
        for key in animDurations.keys():
            self.animDurations[key] = animDurations[key]

        for key in animStateTransitions.keys():
            self.animStateTransitions[key] = animStateTransitions[key]

    def getNextAnimState(self):
        return self.animStateTransitions[self.grState]

    def getCurrentAnimDuration(self):
        return self.animDurations[self.grState]

    def animDurationExists(self):
        if self.grState in self.animDurations:
            return True

        return False

    def stateTransitionExists(self):
        if self.grState in self.animStateTransitions:
            return True

        return False


class Entity(object):
    def __init__(self, id, health, dmg, dmgable, animDuration, 
                 animStateTransitions, world, type):
        self.id = id
        self.gameProps     = EntityGameProps(health, dmg, dmgable)
        self.grProps = EntityGrProps(animDuration, animStateTransitions)
        self.world = world
        self.type = type
        self.body = None

    def __del__(self):
        self.world.DestroyBody(self.body)

    # should be defined by every entity, but not yet being utilized properly
    def move(self):
        pass

    def setGrState(self, grState):
        self.grProps.grState = grState
        self.grProps.animDuration = 0
