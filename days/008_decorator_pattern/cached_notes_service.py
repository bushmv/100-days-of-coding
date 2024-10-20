from typing import List

from db import DB
from note import Note
from notes_service import NotesService


class CachedNotesService(NotesService):
    def __init__(self, db: DB) -> None:
        super().__init__(db)
        self.cache = {}

    def new(self, tag: str, description: str) -> None:
        super().new(tag, description)
        if tag in self.cache:
            self.cache[tag].append(Note(tag, description))

    def search(self, search_tag: str) -> List[Note]:
        if search_tag not in self.cache:
            self.cache[search_tag] = super().search(search_tag)
        return self.cache[search_tag]
