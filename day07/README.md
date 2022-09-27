# Day 7 #
I did not enjoy day 5 which was an intcode challenge - not helped by trying to solve it on an iPad during an intensive care conference! 
So, when day 7 came around and it was yet more intcode I was not delighted.

## Part 1 ##
This was easy. I took the intcode computer from day 5 and turned it into a function so that I could call it repeatedly 
for each amplifier in the circuit. Not a problem. Unfortunately I overwrote the code when I moved on to part 2 and so it doesn't exist 
any more.

## Part 2 ##
Part 2 was a bugger. I eventually realised two things:
1. An amplifier doesn't stop running when it spits out a value - it stops when it needs an input.
2. When looping back round to the start the amplifier should not be in it's initial state, it should be waiting for 
the next input with the same state it was in from the previous loop.

I considered using a list to save the state of each amplifier but eventually rewrote the whole thing using OOP. That's not a technique I 
use very often and so it's not very neat but it seemed like having multiple objects (amplifiers) with their own state is 
kind of what OOP was invented for! Also, I'm using AoC to improve my skills so I *should* push myself to use new techniques.
