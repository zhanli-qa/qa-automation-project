user_list_response_schema = {
    "type": "array",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "password": {"type": "string"}
      },
    "required": ["id"]
}