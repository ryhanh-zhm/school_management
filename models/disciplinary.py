import uuid
from utils.data_manager import load_data, save_data

class DisciplinaryRecord:
    def __init__(self, record_type, description):
        self.id = str(uuid.uuid4())
        self.record_type = record_type
        self.description = description
    
    def _save(self):
        records = load_data("disciplinary.json")
        records[self.id] = self.__dict__
        save_data("disciplinary.json", records)