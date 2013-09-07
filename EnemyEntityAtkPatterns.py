import TypeEnums
import EnemyEntityMovePatterns

def AtkPatternNull(entity):
    return []

def AtkPatternBasic(entity):
    if not hasattr(entity, "atkState"):
        setattr(entity, "atkState", 0)
    
    entity.atkState += 1

    if entity.atkState < 2:
        position = (entity.body.position[0], entity.body.position[1] - 3)
        return [[TypeEnums.BULLET_NORMAL, position, 
                EnemyEntityMovePatterns.MovePatternBasic, AtkPatternNull]]
    else:
        return []

        
