# Trie Search Engine
A search engine using a Trie structure

## How to use 

Install all required packages using pip either locally or in a virtual environment:
```pip install -r requirements```

Run the search.py command: 
```python main.py <search term>```

## Web UI

A web UI is also provided, built on the following technologies: 
- React
- jQuery 
- jQuery UI 
- Flask
- MaterialiseCSS

### To run the UI: 
1.  Ensure all requirements are installed (see above)

2. Set an environment variable to point to the main.py file:
```
export FLASK_APP=main.py 
export FLASK_DEBUG=1
```

3. Run the flask app
```flask run```

4. Open the browser and head to: http://localhost:5000