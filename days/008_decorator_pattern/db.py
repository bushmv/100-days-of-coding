from typing import List, Tuple


# format: <tag><separator><description><new line>
class DB:
    def __init__(self, data_file_path: str) -> None:
        self.data_file_path = data_file_path
        self.separator = "\x1f"  # unit separator

    def insert(self, record: List[str]) -> None:
        with open(self.data_file_path, "a") as f:
            row = self.separator.join(record) + "\n"
            f.write(row)

    def select(self, search_tag: str = None) -> List[Tuple[str, str]]:
        result = []
        with open(self.data_file_path, "r") as f:
            for record in f.readlines():
                row = record.strip().split(self.separator)
                if self._match(row[0], search_tag):
                    result.append(row)
        return result

    def _match(self, tag: str, search_tag: str) -> bool:
        if not search_tag:
            return True
        return tag == search_tag
