# -*- coding: utf-8 -*-
"""
Raghav is currently watching Netflix. He is feeling thrilled after watching Seasons 1, 2 and 3 of 13 Reasons Why, and is desperately waiting for release of Season 4. But the makers of the show are in no mood to release the next season anytime soon. 

The makers of 13 Reasons Why give Raghav a challenge to solve. If he solves this challenge, then they will give exclusive copy of Season 4 to him.

But Raghav is feeling lazy. Can you help him solve this challenge?

Given 3 integers A, B, C. Do the following steps-

Swap A and B.
Multiply A by C.
Add C to B.
Output new values of A and B.

@author: Aabha
"""

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

#Swap A and B
a,b = b,a 

#Multiply A by C
a *= c

#Add C to B
b += c

#output new values of A and B
print(a,b)