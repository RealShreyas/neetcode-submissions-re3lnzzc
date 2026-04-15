class Node:
    def __init__(self, key=None, value=None, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0  # Track size for O(1) check
    
    def insert(self, node):
        # Insert at the end (tail.prev) to maintain LRU property within the freq
        prv = self.tail.prev
        prv.next = node
        node.prev = prv
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
    
    def remove(self, node):
        prv = node.prev
        nx = node.next
        prv.next, nx.prev = nx, prv
        self.size -= 1
        return node

    def remove_front(self):
        if self.size == 0:
            return None
        # Remove the least recently used node in this frequency bucket
        return self.remove(self.head.next)

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map = {}      # key -> Node
        self.freq_map = {}     # freq -> DLL

    def _update_freq(self, node):
        """Helper to move a node to a higher frequency bucket"""
        freq = node.freq
        self.freq_map[freq].remove(node)
        
        # If the current min_freq bucket is empty, increment min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DLL()
        
        self.freq_map[new_freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        node = self.key_map[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.value = value
            self._update_freq(node)
        else:
            if self.size >= self.capacity:
                # Evict the LRU node from the min_freq bucket
                old_node = self.freq_map[self.min_freq].remove_front()
                del self.key_map[old_node.key]
                self.size -= 1
            
            new_node = Node(key, value, 1)
            self.key_map[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DLL()
            
            self.freq_map[1].insert(new_node)
            self.min_freq = 1 # Reset min_freq to 1 for a brand new element
            self.size += 1