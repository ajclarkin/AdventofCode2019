# Day 15 - Oxygen System #
I decided to to a bit of reading about this because it seemed like there would be a specific way to solve it.
It turns out that maze-solving is a fairly common computing challenge. The difference here is that because of the use of the intcode computer
backtracking is not as straight-forward. I put a lot of thought into how to use recursion but I just couldn't see it. I also thought about
forking each time there was a junction (more than two routes out of a box) but I could forsee that becoming unmanageable pretty quickly.

## Part 1 ##
This is really not efficient code - we check all possible moves and undo them before deciding which move to make.

This is Tremaux's algorithm.
https://www.wikiwand.com/en/Maze_solving_algorithm#/Tr%C3%A9maux's_algorithm

* Map all the surrounding squares - if we don't know about an adjacent box then try to move there.
    * Save coordinate to a dictionary recording whether open or wall
    * If open we need to move back to where we were
* Record visit to current square - history dictionary saves hom many times we have been somewhere.
    * If there's no history for this box then set it to 1.
    * If been here before then increment history - this would happen if backtracking out of a dead end.
    * If there is only 1 adjacent open box then it is a dead end - set history to 2.
* Find the next move to make - of all the adjacent non-wall boxes (already saved) - move to the one which has been visited the least.
    * Where we came from will have history of 1.
    * Unexplored path will have history of 0.
    * Explored dead end will have history of 2 (set to 1 on the way out and 2 on the way back).
* Make the move identified.
* If moving takes us to the oxygen port then break out of the loop, otherwise repeat.


# 2022 Status Note
This doesn't work. It hasn't been touched since February 2020. There was a bit of a pandemic and I had to abandon this. It stil annoys me that it's not finished.
What this solution tries is a depth-first search. I believe I need to use a breadth-first search. I don't know anything about graph theory - it's not exactly something
that I use in my daily work. Perhaps I'll get time to come back to this - I hope so. I've deliberately not watched the solution videos on youtube - but there are 
plenty. I believe this is the dungeon master problem.

## Part 1 - SOLVED ##
October 11, 2022. I have finished part 1 and I am sooooo happy.
Breadth-first search, inefficient because I go back to the origin each time and then follow each path in turn.

*Solution*
- Use a list of lists called paths to save all the possible paths from the origin.
- The first entry is created outside of a loop to populate paths and so that we know what the first move is
- Now loop until the return code from a move is 2, that is, the oxygen is found.
- On each iteration remove the oldest path and follow it to the end.
- Find all the valid moves at the end of that path and for each valid move save the path followed with that move appended to paths.
- (So, if the path followed had 10 steps and then there were 3 valid moves at the end of the path then 3 new paths will be saved to the end of paths list.)
- Once the oxygen is found count the length of the latest list which will be the number of steps to it.