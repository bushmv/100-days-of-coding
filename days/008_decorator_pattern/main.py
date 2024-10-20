from cached_notes_service_decorator import CachedNotesServiceDecorator
from censored_notes_service import CensoredNotesService
from censored_notes_service_decorator import CensoredNotesServiceDecorator
from db import DB
from notes_service import NotesService
from sorted_censored_notes_service import SortedCensoredNotesService
from sorted_notes_service import SortedNotesService
from sorted_notes_service_decorator import SortedNotesServiceDecorator

help_message = """Usage:
- new [tag] [description]\n    Create new note with [tag] and [description].
- all\n    Get all notes.
- search [tag]\n    Get notes by tag [tag].
- help\n    Show this message.
- exit\n    Close program."""


def main() -> None:
    db = DB("data.txt")
    ns = NotesService(db)
    while True:
        cmd = input(">>> ")
        match cmd:
            case "new":
                tag = input("tag: ")
                description = input("description: ")
                ns.new(tag, description)
            case "all":
                for note in ns.all():
                    print(note)
            case "search":
                search_tag = input("tag for search: ")
                for note in ns.search(search_tag):
                    print(note)
            case "help":
                print(help_message)
            case "exit":
                break
            case "reset":
                ns = NotesService(db)
            case _:
                print("Unknown command.")


if __name__ == "__main__":
    main()
