class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.elements = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_tail(self, node):
        prv = self.tail.prev
        prv.next = node
        node.prev = prv
        node.next = self.tail
        self.tail.prev = node
        self.elements += 1
    
    def remove_head(self):
        if self.elements == 0:
            return None
        
        return self.remove(self.head.next)
    
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
        
        self.elements -= 1
        return node

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = defaultdict(list)
        self.dll = DLL()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        node = self.mp[key]
        self.dll.remove(node)
        self.dll.insert_tail(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.dll.remove(self.mp[key])
        
        new_node = Node(key, value)
        self.mp[key] = new_node
        self.dll.insert_tail(new_node)

        if self.dll.elements > self.capacity:
            lru_node = self.dll.remove_head()
            if lru_node:
                del self.mp[lru_node.key]