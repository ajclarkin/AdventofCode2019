# Day 13 #
Another intcode challenge using the interpreter developed earlier in the month.


## Part 1 ##
Part one was to create a breakout style arcade game and count the number of blocks on the screen. Easy.
I used a set to store unique locations of blocks and then counted the length of the set.


## Part 2 ##
This took me quite some time. I updated part one to ensure that when an empty or ball tile was generated it 
removed any blocks that existed with the same location. I initially tried making the joystick move left and 
right sequentially - that didn't work. I toyed with random movements (why???). But, this is AoC - it was never
going to be that straight-forward.

I eventually decided to print out the board to make sure I understood what was happening - it was clear at that point 
that the paddle actually needed to contact the ball. I thought about manual control of the joystick but decided to solve 
it programatically. So, the joystick input is now based on where the ball is and calculates where the ball will touch the baseline. 
The inputs are calculated to move the paddle to meet the joystick.

#### Display Output ####
I update the board display using a screen refresh then printing the whole thing again. It flickers and takes ages to run. 
Set self.display = 1  to dispay the board or 0 to hide it - which is much faster.
