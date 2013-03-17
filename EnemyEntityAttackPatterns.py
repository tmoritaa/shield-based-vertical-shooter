import TypeEnums
import EnemyEntityMovePatterns

def AttackPatternNull(entity):
    return []

def AttackPatternBasic(entity):
    if not hasattr(entity, "attackState"):
        setattr(entity, "attackState", 0)
    
    entity.attackState += 1

    if entity.attackState < 2:
        position = (entity.body.position[0], entity.body.position[1] - 3)
        return [[TypeEnums.BULLET_NORMAL, position, 
                EnemyEntityMovePatterns.MovePatternBasic, AttackPatternNull]]
    else:
        return []

        
