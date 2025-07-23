class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.current_size = 0
        self.cache = {}
        # Fix: Initialize MRU first, then LRU
        self.MRU = Node(None, None)
        self.LRU = Node(None, None, None, self.MRU)
        self.MRU.prev = self.LRU
       
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            # Move to front and return value
            node = self.add_to_front(key, self.cache[key].val)
            self.cache[key] = node
            return node.val
        return -1
       
    def add_to_front(self, key, value):
        # Remove node from current position if it exists
        if key in self.cache:
            # O(1) removal using direct node reference from dictionary
            existing_node = self.cache[key]
            existing_node.prev.next = existing_node.next
            existing_node.next.prev = existing_node.prev
        else:
            # New key - check if we need to remove LRU
            if self.current_size >= self.capacity:
                # Remove least recently used (node before MRU)
                lru_node = self.MRU.prev
                # Remove the check - dummy nodes are properly set up
                lru_node.prev.next = lru_node.next
                lru_node.next.prev = lru_node.prev
                del self.cache[lru_node.key]
                self.current_size -= 1
            
            # Increment size for new key
            self.current_size += 1
        
        # Add new node to front (right after LRU)
        new_node = Node(key, value)
        # Direct assignment - LRU.next always exists due to dummy nodes
        new_node.next = self.LRU.next
        new_node.prev = self.LRU
        self.LRU.next.prev = new_node
        self.LRU.next = new_node
        
        return new_node
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # add_to_front handles everything - existence check, LRU removal, etc.
        new_node = self.add_to_front(key, value)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)