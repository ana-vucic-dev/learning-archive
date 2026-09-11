from __future__ import annotations


class ListNode:
    def __init__(self, value: int = 0, next: ListNode | None = None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head: ListNode | None = None

    def is_empty(self) -> bool:
        return self.length == 0

    def add(self, value: int) -> None:
        node = ListNode(value)

        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

        self.length += 1

    def remove(self, value: int) -> None:
        previous = None
        current = self.head

        while current and current.value != value:
            previous = current
            current = current.next

        if not current:
            return
        elif previous:
            previous.next = current.next
        else:
            self.head = current.next

        self.length -= 1


linked_list = LinkedList()

assert linked_list.is_empty() == True

linked_list.add(1)
linked_list.add(2)

assert linked_list.is_empty() == False
assert linked_list.length == 2

linked_list.remove(1)

assert linked_list.length == 1
