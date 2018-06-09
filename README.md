# Trie Search Engine

The following project demonstrates how to write a simple Trie structure to efficiently store search query suggestions.

Implemented functions include logic to: 
- Create a root node of a Trie
- Add words to the trie 
- Look for all words in the trie
- Look for words using a prefix
- List all children of a node within the trie

![screen shot 2018-06-09 at 11 32 10](https://user-images.githubusercontent.com/22529514/41190641-e470bfec-6bda-11e8-9d7f-fd52d4d013df.jpg)

## How to use 

Install all required packages using pip either locally or in a virtual environment:
```pip install -r requirements```

Run the search.py command: 
```python main.py <search term>```

![screen shot 2018-06-09 at 11 48 46](https://user-images.githubusercontent.com/22529514/41190650-18af5cbe-6bdb-11e8-8a38-bc4b3e0a3b91.jpg)


## Web UI

A web UI is also provided, built on the following technologies: 
- React
- jQuery 
- jQuery UI 
- Flask
- MaterialiseCSS

### To run the Web UI: 
1.  Ensure all requirements are installed (see above)

2. Set an environment variable to point to the main.py file:
```
export FLASK_APP=main.py 
export FLASK_DEBUG=1
```

3. Run the flask app
```flask run```

4. Open the browser and head to: http://localhost:5000

Enjoy!
