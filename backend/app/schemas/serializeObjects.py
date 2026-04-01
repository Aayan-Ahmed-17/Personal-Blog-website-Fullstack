def serializeDict(entity) -> dict:
    """
    Takes Monogdb document and converts into dict
    """
    if entity is not None:
        return {
            **{i: str(entity[i]) for i in entity if i == "_id"},
            **{i: entity[i] for i in entity if i != "_id"},
        }  # convert "id" into str and combine both dict into single
    return None  # type: ignore


def serializeList(entities) -> list:
    """
    Takes multiple Monogdb documents and converts into dict return list of dictionary
    """
    return [serializeDict(entity) for entity in entities]
