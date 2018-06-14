import pickle
from functions import (
    create_root_node,
    add_word_to_trie
)

INPUT_FILE = "korean_word_list.txt"
OUTPUT_FILE = "korean_pickle.pkl"

def main():

    with open(f"resources/{INPUT_FILE}") as file:
        raw_content = file.readlines()

    print(f"Size of word document: {len(raw_content)}")

    trie = create_root_node()

    for word in raw_content: 
        add_word_to_trie(trie, word)

    print('''
    Finished inserting words into tree
    Creating and saving pickle...
        ''')

    with open(f"resources/{OUTPUT_FILE}", 'wb') as file: 
        pickle.dump(trie, file)    

    print("Done!")

if __name__ == '__main__':
    main()