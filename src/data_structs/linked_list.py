from typing import Any


class Node:
    def __init__(self, value: Any, next_node: "Node | None") -> None:
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def append(self, value: Any) -> None:
        node = Node(value=value, next_node=None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def add_node(self, value: Any) -> bool:
        self.append(value)
        return True

    def __str__(self) -> str:
        current = self.head
        if current is None:
            return "[None]"

        parts: list[str] = []
        while current is not None:
            value = current.value
            parts.append(str(value))
            current = current.next

        output = " -> ".join(parts)
        output = f"[{output} -> None]"
        return output
