from typing import List

from db import DB
from note import Note
from notes_service import NotesService


class CensoredNotesService(NotesService):
    def __init__(self, db: DB, bad_words: List[str], replace_char: str) -> None:
        super().__init__(db)
        self.bad_words = bad_words
        self.replace_char = replace_char

    def all(self) -> List[Note]:
        notes = super().all()
        for note in notes:
            for word in self.bad_words:
                note.description = note.description.replace(
                    word, self.replace_char * len(word)
                )
        return notes

    def search(self, search_tag: str) -> List[Note]:
        notes = super().search(search_tag)
        for note in notes:
            for word in self.bad_words:
                note.description = note.description.replace(
                    word, self.replace_char * len(word)
                )
        return notes
