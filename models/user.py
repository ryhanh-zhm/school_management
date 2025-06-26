import uuid
from utils.password_generator import generate_password
from utils.data_manager import save_data, load_data


class User:
    def __init__(self, username, role, password=None):
        self.username = username
        self.role = role
        self.password = password or generate_password()
        self.id = str(uuid.uuid4())

    def change_password(self, new_password):
        self.password = new_password
        self._save()
    
    def _save(self):
        users = load_data("users.json")
        users[self.id] = self.__dict__
        save_data("users.json", users)