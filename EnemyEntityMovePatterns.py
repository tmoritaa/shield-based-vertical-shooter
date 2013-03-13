def MovePatternBasic(entity):
    if not hasattr(entity, "moveState"):
        setattr(entity, "moveState", 0)

    entity.moveState += 1

    if entity.moveState < 50:
        entity.body.linearVelocity.x = -1
        entity.body.linearVelocity.y = -1
    elif entity.moveState < 100:
        entity.body.linearVelocity.x = 1
        entity.body.linearVelocity.y = 1
    else:
        entity.moveState = 0
        
