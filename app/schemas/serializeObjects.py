def serializeDict(entity) -> dict:
    if entity is not None:
        return {**{i:str(entity[i]) for i in entity if i=='_id'},**{i:entity[i] for i in entity if i!='_id'}}
    return None # type: ignore

def serializeList(entities) -> list:
    return [serializeDict(entity) for entity in entities]