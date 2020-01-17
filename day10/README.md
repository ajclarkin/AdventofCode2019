# Day 10 #
I really liked this challenge. On first reading I thought *I have no idea how to do this* and within a couple of hours of 
not thinking about it it was clear what I had to do. It was also the first challenge that was written up on the blackboard 
in the kitchen - I'm going to get the wife interested in this if I can!

## Part 1 ##
In effect the question here is how many unique directions are there to asteroids.

I process the input as one long string but break each asteroid out into it's x,y coordinates as required. I used a set for 
storing unique data and calculated the angle to each asteroid using the tangent. I initially tried to use a more simplified direction 
indicator but I think I know all along that some trig was going to be involved.


## Part 2 ##
Did someboday say complete vaporisation by giant laser?

There's a loop in here that could be neater but I'll survive. Built on solution from part 1, angles refactored to begin 
pointing straight up.
