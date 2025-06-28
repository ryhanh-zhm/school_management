import uuid
from utils.data_manager import load_data, save_data

class Letter:
    def __init__(self, sender_id, receiver_id, content):
        users = load_data("users.json")
        if sender_id not in users:
            raise ValueError(f"Sender ID {sender_id} not found in users")
        if receiver_id not in users:
            raise ValueError(f"Receiver ID {receiver_id} not found in users")
        valid_roles = ["admin", "teacher", "student", "parent", "vice_principal"]
        if users[sender_id]["role"] not in valid_roles:
            raise ValueError(f"Invalid sender role: {users[sender_id]['role']}")
        if users[receiver_id]["role"] not in valid_roles:
            raise ValueError(f"Invalid receiver role: {users[receiver_id]['role']}")
        self.id = str(uuid.uuid4())
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self._save()

    def _save(self):
        letters = load_data("letters.json")
        letters[self.id] = self.__dict__
        save_data("letters.json", letters)