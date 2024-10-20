from typing import Any, Callable, List


def ns_sorted(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        notes = func(*args, **kwargs)
        notes.sort(key=lambda note: (note.tag, note.description))
        return notes

    return wrapper


def ns_cached(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Any:
        _, search_tag = args
        if search_tag not in cache:
            cache[search_tag] = func(*args, **kwargs)
        return cache[search_tag]

    return wrapper


def ns_cencored(bad_words: List[str], char_replacer: str) -> Callable:
    def _ns_censored(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            notes = func(*args, **kwargs)
            for note in notes:
                for word in bad_words:
                    note.description = note.description.replace(
                        word, char_replacer * len(word)
                    )
            return notes

        return wrapper

    return _ns_censored
