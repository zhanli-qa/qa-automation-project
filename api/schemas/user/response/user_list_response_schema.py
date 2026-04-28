from api.schemas.user.response.user_response_schema import user_response_schema

user_list_response_schema = {
    "type": "array",
    "items": user_response_schema
}