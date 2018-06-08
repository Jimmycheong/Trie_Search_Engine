import pickle
from functions import (
    create_root_node,
    add_word_to_trie
)

def main():

    with open("resources/word_list.txt") as file:
        raw_content = file.readlines()
        word_list = [x.strip() for x in raw_content] 

    print(f"Size of word document: {len(word_list)}")

    trie = create_root_node()

    for word in word_list: 
        add_word_to_trie(trie, word)

    print('''
    Finished inserting words into tree
    Creating and saving pickle...
        ''')

    with open("resources/trie_obj", 'wb') as file: 
        pickle.dump(trie, file)    

    print("Done!")

if __name__ == '__main__':
    main()