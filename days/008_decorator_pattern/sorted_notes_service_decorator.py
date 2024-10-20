from typing import List
from note import Note
from notes_service import NotesService


class SortedNotesServiceDecorator(NotesService):
    def __init__(self, notes_service: NotesService) -> None:
        self.notes_service = notes_service

    def new(self, tag: str, description: str) -> None:
        self.notes_service.new(tag, description)

    def all(self) -> List[Note]:
        notes = self.notes_service.all()
        notes.sort(key=lambda note: (note.tag, note.description))
        return notes

    def search(self, search_tag: str) -> List[Note]:
        notes = self.notes_service.search(search_tag)
        notes.sort(key=lambda note: (note.rag, note.description))
        return notes
