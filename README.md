# File Locator

File Locator is a simple tool that allows you to locate any file from any local system it is run on. It provides a class-based interface that can be used to search for a specific file within a given directory or the current working directory.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/InevitablePG/FileLocator.git
   ```

2. Navigate to the project directory:

   ```
   cd FileLocator
   ```

3. Install the required dependencies using `pip`:

   ```
   pip install -r requirements.txt
   ```

4. A simple usage using `python`:
   ```
   python3 main.py
   ```

5. Then visit localhost at port `8080`:
   ```
   http://127.0.0.1:8080/
   ```

## Usage

The `FileSearch` class in `FileLocator.py` provides the main functionality of the tool. Here's a basic usage example:

```python
from Locator.FileLocator import FileSearch

# Create an instance of FileSearch
file_search = FileSearch("filename.txt")

# Perform a basic search in the current working directory
results = file_search.Search(advanced=False) # Tick for advanced search

# Perform an advanced search in a specific root directory
results = file_search.Search(advanced=True)

# Then loop through the result
for result in results:
    print(result)
```

By default, the `Search()` method searches for the specified file (`"filename.txt"`) in the current working directory. To perform an advanced search, provide a root directory as the `rootDir` parameter when creating the `FileSearch` instance.

For a complete usage example, refer to the `main.py` file in the repository.

## Project Structure

```
├── Locator
│   ├── FileLocator.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── static
│   └── main.css
└── templates
    └── index.html
```

The project structure follows a typical Flask application structure. The `Locator` directory contains the main logic of the file search, while `static` and `templates` directories hold static files and HTML templates, respectively. The `main.py` file serves as the entry point for the Flask application.


