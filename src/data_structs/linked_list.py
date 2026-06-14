from typing import Any


class Node:
    def __init__(self, value: Any, next_node: "Node | None") -> None:
        self.value: Any = value
        self.next: Node | None = next_node


# Lista enlazada simple
class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0
        self._ids: set[str] = set()

    def is_empty(self) -> bool:
        return self.size == 0

    def contains(self, id: str) -> bool:
        return id in self._ids

    # Inserción de amigos, posts, etc. sin duplicados
    def add_node(self, value: Any, id: str) -> bool:
        if self.contains(id):
            return False
        self._append(value)
        self._ids.add(id)
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
