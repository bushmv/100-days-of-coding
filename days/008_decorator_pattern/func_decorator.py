from typing import Callable, List

from db import DB
from note import Note
from notes_service import NotesService


def set_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> List[Note]:
        print("before")
        notes = func(*args, **kwargs)
        print("after")
        return notes

    return wrapper


def main() -> None:
    db = DB("data.txt")
    notes_service = NotesService(db)
    for note in notes_service.all():
        print(note)


if __name__ == "__main__":
    main()
