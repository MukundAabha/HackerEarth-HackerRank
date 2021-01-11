# -*- coding: utf-8 -*-
"""
Problem :
    Mike wants to go fishing this weekend to nearby lake. 
    His neighbour Alice (is the one Mike was hoping to ask out since long time) is also planing to go
    to the same spot for fishing this weekend. The probability that it will rain this weekend is p1. 
    There are two possible ways to reach the fishing spot (bus or train). 
    The probability that Mike will take the bus is pmb and that Alice will take the bus is pab .
    Travel plans of both are independent of each other and rain.

What is the probability prs that Mike and Alice meet each other only 
(should not meet in bus or train) in a romantic setup (on a lake in rain)?

@author: Aabha
"""

pmb = eval(input())
pab = eval(input())
p1 = eval(input())
result = p1*((pmb*(1-pab)+pab*(1-pmb)))
print("{0:0.6f}".format(result))


"""
Explanation:
the probability of mike taking the bus and the probability that alice doesn't take the bus is (pmb*(1-pab))
the probability of alice taking the bus and the probability that mike doesn't take the bus is (pab*(1-pmb))
then the probability that they meet is pmb*(1-pab)+pab*(1-pmb)
then the probability that they meet on romantic (rainy day) is p1*(pmb*(1-pab)+pab*(1-pmb))
and Hence you get the answer
    
"""