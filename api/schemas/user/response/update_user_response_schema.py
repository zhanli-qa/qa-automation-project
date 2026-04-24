update_user_response_schema = {
  "type": "object",
  "properties": {
    "username": {"type": "string"},
    "email": {"type": "string"},
    "password": {"type": "string"}
  },
  "required": ["username", "email"],
  "additionalProperties": True
}