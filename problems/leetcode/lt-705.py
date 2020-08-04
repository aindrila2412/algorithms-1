# 705. Design HashSet
"""
	
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

	- add(value): Insert a value into the HashSet. 
	- contains(value) : Return whether the value exists in the HashSet or not.
	- remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""
class MyHashSet:
    def __init__(self):
        """
        Initialise your data structure here.
        """
        self.hashSet = [[] for i in range(10000)]
        
    def hash_function(self, key) -> int:
        return key % 10000
        
    def add(self, key: int) -> None:
        hash_key = self.hash_function(key)
        if key not in self.hashSet[hash_key]:
            self.hashSet[hash_key].append(key)
    
    def remove(self, key: int) -> None:
        hash_key = self.hash_function(key)
        if key in self.hashSet[hash_key]:
            self.hashSet[hash_key].remove(key)
            
    def contains(self, key: int) -> bool:
        hash_key = self.hash_function(key)
        if key in self.hashSet[hash_key]:
            return True