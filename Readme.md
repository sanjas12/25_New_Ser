# Title

# Contents

## Installation

### Prerequisites (Server-Ubuntu) 82.146.47.129


### Prerequisites (Windows)
1. install https://visualstudio.microsoft.com/visual-cpp-build-tools/ 
2. install https://www.sqlite.org/download.html
    2.1. Download the "sqlite-amalgamation" ZIP file.
    2.2. Extract the contents of the ZIP file to a C:\sqlite.
    2.3. Open CMD ->  and set the SQLite3_INCLUDE_DIR environment variable             
    (set SQLite3_INCLUDE_DIR=C:\sqlite)
3. install list-extensions for vscode
4. pip install -r requirement.txt
5. python3 setup.py build 
<!-- 6. python -c "import sqlite3; print(sqlite3.sqlite_version)"   -->

### Usage (Windows)
1. source .env
2. python main.py

### Usage (Ubuntu)
cat -e -t -v Makefile      <!-- check makefile -->
make -f Makefile.win run

### TODO

### help
https://realpython.com/python-web-scraping-practical-introduction/