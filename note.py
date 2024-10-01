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

def get_new_id():
    if not notes: #is empty
        return 0
    else:
        return max(notes.keys()) + 1

def add():
    print("The note name:")
    name = input()
    print("The note:")
    body = input()
    update(Note(get_new_id(), name, body))

def edit():
    print("Specify note id, which you want to edit:")
    id = int(input())
    if id in notes.keys():
        print("The new note name:")
        name = input()
        print("The new note:")
        body = input()
        existed_note = notes.get(id)
        existed_note.name = name
        existed_note.body = body
        existed_note.updatedAt = now_str()
        update(existed_note)
    else:
        print("Such note does not exists")
        
def delete():
    print("Specify note id to delete")
    id = int(input())
    if id in notes.keys():
        notes.pop(id)
    else:
        print("Such note does not exists")

def print_notes():
    print("Print all notes:")
    for note in notes.values():
        print(note)
    print("====")

def print_by_id():
    print("Specify id:")
    id = int(input())
    if id in notes.keys():
        print(notes.get(id))
    else:
        print("Such note does not exists")

def print_by_created_date():
    print("Specify date in format Y-m-d:")
    date = dt.strptime(input(), "%Y-%m-%d").date()
    filtered = []
    for note in notes.values():
        createdAt = dt.strptime(note.createdAt, datetime_pattern).date()
        if (createdAt == date):
            filtered.append(note)
    print(filtered)

def print_by_updated_date():
    print("Specify date in format Y-m-d:")
    date = dt.strptime(input(), "%Y-%m-%d").date()
    filtered = []
    for note in notes.values():
        updatedAt = dt.strptime(note.updatedAt, datetime_pattern).date()
        if (updatedAt == date):
            filtered.append(note)
    print(filtered)
