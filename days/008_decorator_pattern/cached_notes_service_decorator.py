from typing import List

from note import Note
from notes_service import NotesService


class CachedNotesServiceDecorator(NotesService):
    def __init__(self, notes_service: NotesService) -> None:
        self.notes_service = notes_service
        self.cache = {}

    def new(self, tag: str, description: str) -> None:
        if tag in self.cache:
            self.cache[tag].append(Note(tag, description))
        self.notes_service.new(tag, description)

    def all(self) -> List[Note]:
        return self.notes_service.all()

    def search(self, search_tag: str) -> List[Note]:
        if search_tag not in self.cache:
            self.cache[search_tag] = self.notes_service.search(search_tag)
        return self.cache[search_tag]
