import datetime
from datetime import datetime as dt

datetime_pattern = "%Y-%m-%d, %H:%M:%S"

def now_str():
    return dt.now().strftime(datetime_pattern)

class Note:
    def __repr__(self):
        return f"Note {self.id}\nname is: {self.name}\nbody is: {self.body}\nlast updated at: {self.updatedAt}\ncreated at: {self.createdAt}\n-------"

    def __str__(self):
        return f"Note {self.id}\nname is: {self.name}\nbody is: {self.body}\nlast updated at: {self.updatedAt}\ncreated at: {self.createdAt}\n-------"

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def __init__(self, id, name, body):
        self.id = id
        self.name = name
        self.body = body
        self.updatedAt = now_str()
        self.createdAt = now_str()

notes = {}
