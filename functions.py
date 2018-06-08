from typing import List
from node import Node


def look_for_words_beginning_with(node: Node, prefix: str) -> List[str]:
    
    ''' 
    Takes a prefix string and searches a trie for words

    Params:
        node (Node): A root node representing the root of a Trie structure
        prefix(str): A str containing the prefix of a desired search word 

    Returns: 
        results (List[str]): A list of words beginning with the prefix requested

    '''

    original = node
    results = []
    for char in prefix: 
        if char in check_children_letters(node):
            child_index = check_children_letters(node).index(char)
            node = node.children[child_index]

    if node != original:
        endings_list = look_for_words(node, "")
        prepended_words = list(map(lambda s: prefix + s, endings_list))
        results += prepended_words

    return results

def look_for_words(node: Node, accumulated: str) -> List[str]: 

    '''
    Recursive search of all words in a trie structure. Base condition returns if the
    last letter actually creates a word. Continues to recursively search for more words
    if child nodes exist.

        Params:
        node (Node): Any node within a trie structure
        accumulated: A str containing letters gathered from higher parents 

    Returns: 
        results (List[str]): A list of words 
    '''

    results = []

    if node.is_a_word:
        results += [accumulated]

    if len(node.children) > 0:
        for child in node.children:
            results += look_for_words(child, accumulated + child.letter)
    return results

def create_root_node():
    '''
    Create a root node representing the root node of a trie

    Returns:
        Node: an Node instance containing representing an empty Trie

    '''
    return Node("*")

def check_children_letters(node: Node):
    '''
    Returns a list of strings representing the letters for each child node in the list passed in

    Args: 
        list_(List[Node]): 

    Returns:
        A list of characters for each Node
    '''

    return list(map(lambda s: s.letter, node.children))

def get_child_node(parent: Node, char: str) -> Node:

    '''
    TODO: Finish definition
    '''

    filtered = list(filter(lambda s: s.letter == char , parent.children))
    return filtered[0]

def add_word_to_trie(node: Node, word: str):

    '''     
    TODO: 

    Adds a new word to the trie structure
    
    '''
    for char in word: 
        children_letters = check_children_letters(node)
        if char not in children_letters:
            node.children += [Node(char)]
        child_node = get_child_node(node, char)
        node = child_node
    node.is_a_word = True

def find_prefix(root, prefix: str): 
    
    '''
    TODO: 
    '''

    node = root 
    for char in prefix:         
        print(f"list of children: {check_children_letters(node)}")
        if char not in check_children_letters(node):
            print(f"not found at char: {char}")
            return False 
        node = get_child_node(node, char)
    print("found!")
    return True

# def display_suggestions(root: Node, prefix: str):
#     '''
#     Returns a List of suggestions based on a prefix
    

#     Recursive method. 

#     Base condition: 
#     - if the node is a word then return the word
#     - if the node has more children, search through each child


#     Logic: 
#     - append new words to the search_results array

#     '''

#     node = root
#     suggestions = []
#     accumulated = ""

#     for i, char in enumerate(prefix):
#         accumulated += char
#         if i > 2:
#             suggestions += look_for_words(node, accumulated)

#     return suggestions

