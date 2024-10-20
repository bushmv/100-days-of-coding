from typing import Callable, List

from db import DB
from note import Note
from decorators import ns_cached, ns_sorted, ns_cencored


class NotesService:
    def __init__(self, db: DB) -> None:
        self.db = db  # aggregation
        # self.db = DB("data.txt") - composition

    def new(self, tag: str, description: str) -> None:
        self.db.insert((tag, description))

    # open-closed principle
    @ns_sorted
    @ns_cencored(bad_words=["not"], char_replacer="*")
    def all(self) -> List[Note]:
        print("Load notes")
        records = self.db.select()
        return [Note(*line) for line in records]

    @ns_cached
    @ns_sorted  # ns_sorted(search)
    @ns_cencored(bad_words=["rst"], char_replacer="+")  # ns_cencored()(search)
    def search(self, search_tag: str) -> List[Note]:
        records = self.db.select(search_tag)
        return [Note(*line) for line in records]
