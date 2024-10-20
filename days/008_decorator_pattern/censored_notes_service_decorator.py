from typing import List

from note import Note
from notes_service import NotesService


class CensoredNotesServiceDecorator(NotesService):
    def __init__(
        self, notes_service: NotesService, filter_list: List[str], placeholder: str
    ) -> None:
        self.notes_service = notes_service
        self.filter_list = filter_list
        self.placeholder = placeholder

    def new(self, tag: str, description: str) -> None:
        self.notes_service.new(tag, description)

    def all(self) -> List[Note]:
        notes = self.notes_service.all()
        for note in notes:
            for word in self.filter_list:
                note.description = note.description.replace(
                    word, self.placeholder * len(word)
                )
        return notes

    def search(self, search_tag: str) -> List[Note]:
        notes = self.notes_service.search(search_tag)
        for note in notes:
            for word in self.filter_list:
                note.description = note.description.replace(
                    word, self.placeholder * len(word)
                )
        return notes
