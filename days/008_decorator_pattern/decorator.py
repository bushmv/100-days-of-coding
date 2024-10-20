from typing import List

from db import DB
from note import Note
from notes_service import NotesService


class Decorator(NotesService):
    def __init__(self, notes_service: NotesService):
        self.notes_service = notes_service

    def new(self, tag: str, description: str) -> None:
        return self.notes_service.new(tag, description)

    def all(self) -> List[Note]:
        notes = self.notes_service.all()
        return notes

    def search(self, search_tag: str) -> List[Note]:
        return self.notes_service.search(search_tag)


def main() -> None:
    db = DB("data.txt")
    notes_service = NotesService(db)
    notes_service = Decorator(notes_service)
    for note in notes_service.all():
        print(note)


if __name__ == "__main__":
    main()
