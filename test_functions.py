from node import Node
from functions import (
	create_root_node, 
	add_word_to_trie, 
	find_prefix, 
	look_for_words, 
	look_for_words_beginning_with,
	)
from grappa import should

import pytest

def get_single_child(parent: Node):
	return parent.children[0]

'''FIXTURES '''

SAMPLE_LIST = ["alpha", "alphabet", "alphanumeric",\
					"word", "words", "work", \
					"beta","beer", "baller"
					]

@pytest.fixture
def prepopulated_trie():

	root = create_root_node()

	for word in SAMPLE_LIST:
		add_word_to_trie(root, word)

	return root

'''
TESTS

'''

def test_look_for_words_beginning_with(prepopulated_trie):

	root = prepopulated_trie

	# Case where prefix displays all results
	results_1 = look_for_words_beginning_with(root, "alp")
	sorted(results_1) | should.be.equal.to(["alpha", "alphabet", "alphanumeric"])

	# Case where prefix does not include words within the prefix e.g. 'word'
	results_2 = look_for_words_beginning_with(root, "words")
	sorted(results_2) | should.be.equal.to(["words"])

	# Case where prefix with no words in trie
	results_3 = look_for_words_beginning_with(root, "dis")
	sorted(results_3) | should.be.equal.to([])

def test_look_for_words(prepopulated_trie):	

	root = prepopulated_trie

	results = look_for_words(root, "")

	results | should.be.equal.to(SAMPLE_LIST)


def test_add_word_to_trie():
	root = create_root_node()

	add_word_to_trie(root, "mood")

	child_1 = get_single_child(root)
	child_1.letter | should.be.equal.to("m")

	child_2 = get_single_child(child_1)
	child_2.letter | should.be.equal.to("o")

	child_3 = get_single_child(child_2)
	child_4 = get_single_child(child_3)

	child_4.is_a_word | should.be.true

def test_find_prefix():
	root, child_1, child_2, child_3 = Node("*"), Node("A"), Node("B"), Node("C")

	root.children = [child_1]
	child_1.children = [child_2]
	child_2.children = [child_3]

	is_found = find_prefix(root, "ABC")

	is_found | should.be.equal.true
