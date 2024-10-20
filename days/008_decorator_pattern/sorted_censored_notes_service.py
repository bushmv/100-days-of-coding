from typing import List

from db import DB
from note import Note
from notes_service import NotesService


class SortedCensoredNotesService(NotesService):
    def __init__(self, db: DB, censored_words: List[str], replacer: str) -> None:
        super().__init__(db)
        self.censored_words = censored_words
        self.replacer = replacer

    def all(self) -> List[Note]:
        notes = super().all()
        self._sort_and_then_censor(notes)
        return notes

    def search(self, search_tag: str) -> List[Note]:
        notes = super().search(search_tag)
        self._sort_and_then_censor(notes)
        return notes

    def _sort_and_then_censor(self, notes) -> None:
        notes.sort(key=lambda note: (note.tag, note.description))
        for note in notes:
            for word in self.censored_words:
                note.description = note.description.replace(
                    word, self.replacer * len(word)
                )
