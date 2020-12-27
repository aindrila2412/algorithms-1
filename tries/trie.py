"""
Implementation of Trie Data Structure 
"""
class TrieNode:
    """ A node in the trie data structure """
    def __init__(self, char):
        self.char = char 
        # Check if the node is the end of the word and is not connected to further nodes as False initially 
        self.is_end = False 
        # Counter element to check the number of times elements are inserted into the node 
        self.counter = 0 
        # Dictionary to keep the details of all the connected nodes, empty dict initially 
        self.children = dict()

""" Main Trie Data Structure Class """ 
class Trie:
    """ Constructor method """ 
    def __init__(self):
        """ Initialise the root node, as the trie has at least the root node. 
            The root node does not store any character. 
        """
        self.root = TrieNode("")

    def insert(self, word):
        """ Insert a word into the trie data structure """
        node = self.root 
        # Loop over each character in the word 
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # Create a new node 
                new_node = TrieNode(char)
                # Link the new node to the current character of the parent map 
                node.children[char] = new_node 
                node = new_node
        # Mark the node as the end node 
        node.is_end = True 
        # Increment the node counter 
        node.counter += 1 

    def search(self, word):
        self.output = []
        node = self.root

        # Iterate over 
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        # DFS traversal 
        self.dfs(node, word[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda word: word[1], reverse=True)

    def dfs(self, node, prefix):
        """
            Depth First Search traversal 
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)


x = Trie()
x.insert('hello')
x.insert('hellos')
x.insert('hells')
x.insert('hallo')
x.insert('hello')
x.insert('huku')
print(x.search('he'))
