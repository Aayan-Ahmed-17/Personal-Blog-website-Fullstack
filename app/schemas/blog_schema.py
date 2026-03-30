def blogEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author_name": str(item["author_name"]),
        "author_email": str(item["author_email"]),
        "title": str(item["title"]),
        "description": str(item["description"]),
        "created_at": item["created_at"],
        "updated_at": item["updated_at"],
    }


def blogsEntities(entities) -> list:
    return [blogEntity(item) for item in entities]
