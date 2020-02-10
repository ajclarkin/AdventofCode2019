# Day 14 - Space Stoichiometry #
I hate this. Hate it, hate it, hate it. It took me bloody ages. I was initially quite excited by the thought of it - it looked like 
another good opportunity to use regular expressions and get my head around those. There was a big step in difficulty though.

The code is really ugly for this. It got a bit better when I broke some of it out into mod_equations but still not great.
For an example see part1_failed - it's horrible!

# Mod Equations #
This creates two dictionaries (documented in the file);
equations: there is a dictionary entry for every product in the input list and it contains the components of that product and how many are required
levels: for each product it records how many levels out from ORE it features

Levels lets me process products starting with those furthest from ORE so that I don't expand something and then find more of it gets generated
further down the line.

## Part 1 ##
I use a dictionary called expansion. It starts with {FUEL: 1} and successively replaces each item with the components required to make
the item.

Initially only efficient expansions are made: only expand an item if there are enough of them. For example, if I have 14Z and need 10Z to make
1Y then I can do an efficient expansion and end up with {Z:4, Y:1} - I keep the remainder. Once I can't do efficient expansions any more
I start doing ineffiecient expansions: starting with the highest level. In this example {Z:4, Y:1} would become {Y:2} and because we
know it's inefficient (and hopefully the last time we will use Z because we're working from high levels down) we discard the remainder.

The big difficulty was in managing the remainders. In part1_failed.py I didn't use levels - I did efficient, then ineffecient expansions.
I saved the base units (level 1) for last. It worked for all the examples but not the actual input. I tried forgetting about remainders but
that didn't help. Eventually I thought of using levels to try to minimise the remainders generated and that worked.

## Part 2 ##
Use a binary search - repeatedly halving the search space until find the result. Each iteration we try a value of fuel and see how many ore are required. Keep iterating until the highest value of fuel is found that required <= 1 trillion (1e12) ore.
