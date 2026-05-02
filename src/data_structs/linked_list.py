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

    def print_list(self) -> None:
        current = self.head
        if current is None:
            print("(vacio)")
            return

        output = ""
        while current is not None:
            value = current.value
            if output:
                output += " -> "
            output += str(value)
            current = current.next

        print(output)
