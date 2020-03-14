Word Search Kata
================
## Introduction
For the kata exercise, I decided to implement this using Python. I personally developed and testing using Python 3.7; however, my code should also be compatible with Python2 as well.

I decided to break my implementation into two files: "word_search_problem.py" and "word_search_solver.py".

"word_search_problem" holds the logic for parsing a given file and creating a Puzzle and Word bankk from it.
"word_search_solver" holds the logic for actually solving a given word search.

All of my tests are implemented in the "test_word_search.py" file and the tests were implemented using Python's "unittest" module.

Also, if you wanted to see if this program can solve your own custom word search puzzle, this is the file that allows you to do so "word_search.py"

I'll leave a list of all modules I used below:
```
os
sys
unittest
```

## Running the Application
If you want to run the solution itself you can run either:
```
python3 word_search.py
```
or 
```
python3 word_search.py <path-to-file>
```
The first command will default to using the example_1.txt file in the text_files folder. The second one will allow you to specify a word search puzzle.

If you want to run the tests, run the following command: 
```
python test_word_search.py -v
```
You don't need the -v for this command, but using it gives a bit more details as to which tests pass or fail.

## Future Improvements
Even though I did solve this problem, there are definitely things I would do if I had more time. 

I would focus on writing more tests validating the input file. I didn't focus on that as much because the instructions gave me the impression that I could assume the input would always be valid.
I would add cases ensuring all the the puzzle fields were one character only and were values between 'A' - 'Z'. I would also add checks to ensure the puzzle's length and width are the same.

Besides that, there would be some minor cleanup I would do in the WordSearchSolver class as well as potenitally see if I can improve its efficiency.
