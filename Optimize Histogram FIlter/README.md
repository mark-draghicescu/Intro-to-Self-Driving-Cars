# Project Overview

Now it's time to apply what you've learned to Andy's histogram filter. In his code, you will find eight C++ files. Six of these files contain histogram filter functions. The other two are a main.cpp file and a file containing a function for printing out a matrix.

Your challenge is to read through his files, run the program, and then get his code to run faster.

This project is non-graded, so we are also providing a solution for you in the section labeled "Solution Code". There is not necessarily a wrong and right answer to this project; the goal is to get the code to run faster. The example solution shows a few possible ways to optimize.

# Project Files

In the next part of the lesson, you will find an embedded workspace that contains the following files and folders:

andy_histogram_filter folder
optimized code folder
instructions.md file
andy_histogram_filter
The andy_histogram_filter folder contains Andy's histogram filter code. There is a main.cpp file that runs and times each function of the histogram filter. The time results are outputted to the terminal.

The other .cpp files contain function definitions for the histogram filter.

optimized_code
The optimized_code folder contains a copy of Andy's histogram filter code as well. This is where you can tweak the code for optimization. These files have extra comments giving some ideas about what to optimize.

instructions.md
This file contains further instructions about how to complete and run the project.

hints.md
The optimized_code files already have ideas about what to optimize. The hints file contains more explicit ideas but does not give the actual code. You are not required to read this file, and we encourage you to try optimizing the code first before reading the hints file.

# Explanation of the Code

Here is an explanation of how the histogram filter code works.

In main.cpp, you'll find a vector called grid. Grid is a char vector holding the color values of a 2-dimensional square grid.

The initialize_beliefs function takes in the char grid and outputs the initial probabilities for each square on the grid.

Then the sense function takes a measurement of the current grid space's color. The measurement is used to update the probabilities of each space on the grid.

Next, the blur function passes the grid through a smoothing algorithm.

Then the probabilities are normalized with the normalize function.

Finally, the robot moves to a new space on the board, and the probabilities are updated appropriately.

Each function is run ten-thousand times. You can adjust the number of times by changing the value in the iterations variable.

# Order

As a suggestion, do the project in the following order:

Read through the instructions in instructions.md
Run the code in the andy_histogram_filter folder (see instructions.md for how to run the code)
Open main.cpp and look through the code. You do not need to change anything in this file. Note that each function is run the same number of times. And each function is wrapped with a clock.
Read through each of the .cpp files to become familiar with the code.
Optimize the code in the optimized_code folder. For each optimization, make sure to run the code to see if the results have in fact improved.

Here is a suggested order for optimizing the files:

zeros.cpp
initialize_beliefs.cpp
sense.cpp
blur.cpp
normalize.cpp
move.cpp
