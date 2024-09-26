from typing import Any


class QueueIsFullException(Exception):
    pass


class QueueIsEmptyException(Exception):
    pass


class CircularQueue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.tail = 0
        self.head = 0
        self.size = 0

    def enqueue(self, value: Any) -> None:
        if self.full():
            raise QueueIsFullException()
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self) -> Any:
        if self.empty():
            raise QueueIsEmptyException()
        value = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def empty(self) -> bool:
        return self.size == 0

    def full(self) -> bool:
        return self.size == self.capacity


def main() -> None:
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(cq.dequeue())
    print(cq.dequeue())
    cq.enqueue(4)
    print(cq.dequeue())
    cq.enqueue(5)
    print(cq.dequeue())
    print(cq.dequeue())


if __name__ == "__main__":
    main()
