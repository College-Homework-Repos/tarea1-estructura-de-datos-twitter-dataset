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

    def is_empty(self) -> bool:
        return self.size == 0

    def contains(self, id: str) -> bool:
        current = self.head
        while current is not None:
            if type(current.value) == str:
                if current.value == id:
                    return True
            elif current.value.id == id:
                return True
            current = current.next
        return False

    def add_node(self, value: Any, id: str) -> bool:
        if self.contains(id):
            return False
        self._append(value)
        return True

    def _append(self, value: Any) -> None:
        node = Node(value=value, next_node=None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    # my_lista = LinkedList()
    # len(my_lista)
    def __len__(self) -> int:
        return self.size

    # my_lista = LinkedList()
    # print(my_lista)
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
