## What this is
A trivial script for traversing pages on Wikipedia. What that means is you can provide the title of a page to start at and the script will reiteratively move to the page from either the first or last link of the page a given number of times. What you can get is something like this -
```
Traverse using last links found in pages (Y/N)? N
Title of initial page: lamborghini
Length of traversal: 10

Italy
Geographic coordinate system
Coordinate system
Geometry
Ancient Greek language
Greek language
Modern Greek
Colloquialism
Linguistics
Science
```

## Usage
Make sure the Python interpreter is added to your path and you're good to go :thumbsup:
```
git clone https://github.com/calebwin/wikipedia-traversal.git
cd wikipedia-traversal
python wikipedia_traversal.py
```
