from dataclasses import dataclass


@dataclass
class Note:
    tag: str
    description: str

    def __str__(self):
        return f"[{self.tag}]: {self.description}"
