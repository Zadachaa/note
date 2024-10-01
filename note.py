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

def update(note):
    notes.update({note.id : note})

def dump():
    json_notes = {}
    for note in notes.values():
        json_notes.update({note.id : note.toJson()})
    json.dump( json_notes, open( "notes_dump.json", 'w' ) )

def load():
    json_notes = json.load( open( "notes_dump.json" ) )
    global notes
    notes = {}
    for note_str in json_notes.values():
        json_note = json.loads(note_str)
        note = Note(json_note['id'], json_note['name'], json_note['body'])
        note.updatedAt = json_note['updatedAt']
        note.createdAt = json_note['createdAt']
        update(note)
