import pickle 
import sys

from functions import look_for_words_beginning_with

def main(prefix):
	
    with open("resources/trie_obj", 'rb') as file:
        trie = pickle.load(file)

    suggestions = look_for_words_beginning_with(trie, prefix)

    print(f"Complete list of suggestions: {suggestions}")

if __name__ == '__main__':


    if len(sys.argv) != 2: 
        raise IOError("Please enter a single keyword to search")

    prefix = sys.argv[1]
    print("prefix: {}".format(prefix))
    main(prefix)