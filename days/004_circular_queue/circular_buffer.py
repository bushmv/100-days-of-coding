from typing import Any


class CircularBuffer:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.buffer = [None] * self.capacity
        self.ptr = 0

    def put(self, value: Any) -> None:
        self.buffer[self.ptr % self.capacity] = value
        self.ptr += 1

    def __str__(self) -> str:
        return str(self.buffer)


def main() -> None:
    cb = CircularBuffer(4)
    for i in range(100):
        cb.put(i)
    print(cb)


if __name__ == "__main__":
    main()
