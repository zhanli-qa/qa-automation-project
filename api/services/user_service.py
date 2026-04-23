class UserService:

    def __init__(self, client):
        self.client = client

    def get_all_users(self):
        """
        Get all users
        """
        return self.client.get("/users")

    def get_user_by_id(self, user_id):
        """
        Get single user by id
        """
        return self.client.get(f"/users/{user_id}")

    def create_user(self, payload):
        """
        Create a new user
        """
        return self.client.post("/users", payload)

