class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, value):
        if not self.head:
            return False

        # Case 1: delete head
        if self.head.value == value:
            self.head = self.head.next
            return True

        # Case 2: delete deeper in the list
        prev = self.head
        curr = self.head.next
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next

        return False

    # Optional helper to view the list
    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.value)
            curr = curr.next
        return result


# -------------------
# Example usage
# -------------------
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_head(3)
    ll.insert_at_head(2)
    ll.insert_at_head(1)
    ll.insert_at_tail(4)
    ll.insert_at_tail(5)

    print("List:", ll.to_list())

    ll.delete(3)
    print("After deleting 3:", ll.to_list())

    ll.delete(1)
    print("After deleting 1 (head):", ll.to_list())
