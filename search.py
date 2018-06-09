'''search.py

A program built to search for words using a prefix

'''
import pickle 
import sys

from functions import look_for_words_beginning_with

LINE = "---"

def main(prefix):
	
    with open("resources/trie_obj", 'rb') as file:
        trie = pickle.load(file)

    suggestions = look_for_words_beginning_with(trie, prefix)

    print(f'''
        Search term: {prefix}

        {LINE * 10}
        Complete list of suggestions: 
        {LINE * 10}
        ''')
    for word in suggestions: 
        print(f'''\t{word}''')

    print(f"\t{LINE * 10} \n")


if __name__ == '__main__':

    if len(sys.argv) != 2: 
        raise IOError("Please enter a single keyword to search")

    prefix = sys.argv[1]
    print("prefix: {}".format(prefix))
    main(prefix)
