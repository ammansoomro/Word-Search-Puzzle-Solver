# Word Search Puzzle Solver
This repository contains a Python script for solving word search puzzles. Given a puzzle and a list of words to find, the script finds the positions of each word in the puzzle and returns a colored display of the puzzle with the found words highlighted.

## Installation
This script requires Python run. No additional libraries or packages are required.

## Usage
To use this script, simply import the wordsearch function and provide the puzzle and word list as arguments. The wordsearch function will then return a colored display of the puzzle with the found words highlighted.

``` from wordsearch import wordsearch

# Define puzzle and word list
puzzle = [
    ['T', 'A', 'T', 'I'],
    ['M', 'E', 'E', 'T'],
    ['O', 'C', 'E', 'A'],
    ['F', 'F', 'I', 'E']
]

wordlist = ['TIME', 'TEA', 'ATE', 'OFF']

# Call wordsearch function
wordsearch(puzzle, wordlist)

```


<img width="500" alt="Screenshot 2023-05-11 at 5 01 05 AM" src="https://github.com/ammansoomro/Word-Search-Puzzle-Solver/assets/63865428/408d38de-1d72-4501-9d25-e331fba3bdc2">
