def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author_name": str(item["author_name"]),
        "author_email": str(item["author_email"]),
        "title" : int(item["title"]),
        "description": str(item["description"]),
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
    }

def usersEntities(entities) -> list:
    return [userEntity(item) for item in entities]