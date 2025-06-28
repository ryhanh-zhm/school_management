from models.user import User

class VicePrincipal(User):
    def __init__(self, username):
        super().__init__(username, "vice_principal")