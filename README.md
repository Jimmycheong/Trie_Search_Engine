# Trie Search Engine
A search engine using a Trie structure

## How to use 

```python main.py <search term>```


## Issues 

1. Searching for real words but twice (e.g. beebee) generates bad results:

```['beebee', 'beebeen', 'beebeer', 'beebeef']```


## Future Development

1. Create Flask API services which uses the trie model to 
    provide suggestions for search terms.
2. API service provides web interface which input bar to provide 
real time suggetions