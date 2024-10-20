from typing import List

from db import DB
from note import Note
from notes_service import NotesService


class SortedNotesService(NotesService):
    def __init__(self, db: DB) -> Note:
        super().__init__(db)

    def all(self) -> List[Note]:
        notes = super().all()
        notes.sort(key=lambda note: (note.tag, note.description))
        return notes

    def search(self, search_tag: str) -> List[Note]:
        notes = super().search(search_tag)
        notes.sort(key=lambda note: note.description)
        return notes
