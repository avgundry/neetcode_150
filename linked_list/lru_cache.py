from typing import Optional

from typing import Optional

class LRUCache:
    # Doubly-linked list.
    class Node:
        def __init__(self, key, val: int, nxt, prev):
            self.key = key
            self.val = val
            self.next = nxt
            self.prev = prev

        # def __repr__(self):
        #     return f"Node({self.key}, {self.val}, {self.next})"


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Maps keys to the node with the given value. 
        self.map = dict()
        # Head is LRU
        self.head = None
        # Tail is most recently used
        self.tail = None

    def _update(self, node):
        # Updates the given node to be the most recently used.
        if node == self.head:
            if node.next == None:
                self.tail = node
                return
            else:
                self.head = node.next
        if node != self.tail:
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
        # If the node == tail, it's already at the end so no need to update.
        

    def get(self, key: int) -> int:
        node = self.map.get(key, -1)
        if node == -1:
            return node
        # in this case, need to update it to be at the end of the list.
        self._update(node)

        # print(f"getting {key}: returning {node.val}")
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)
        if node != None:
            # We only update the given node, which already exists.
            node.val = value
            self._update(node)
        else:
            new = self.Node(key, value, None, None)
            self.map[key] = new
            
            if self.head == None and self.tail == None:
                self.head = new
                self.tail = new
            # elif self.head == None:
            #     print("ERROR no head")
            # elif self.tail == None:
            #     print("ERROR no tail")
            else:
                # print(f"updating LL {self.head}\n with new node {new}")
                self._update(new)
                # print(f"updated LL: {self.head}\n")

            if self.size == self.capacity:
                del self.map[self.head.key]
                self.head = self.head.next
                self.head.prev = None
            else:
                self.size += 1

        # print(f"dictionary now: {self.map.items()}")
        # print(f"LL now: {self.head}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)