# -*- coding: utf-8 -*-
"""
Bob has an important meeting tomorrow and he has to reach office on time in morning. 
His general mode of transport is by car and on a regular day (no car trouble) the probability that
 he will reach on time is Pot . The probability that he might have car trouble is Pct .
 If the car runs into trouble he will have to take a train and only 2 trains out of the available N 
 trains will get him to office on time.

What are the chances that he will reach office on time tomorrow?

@author: Aabha
"""
from decimal import Decimal
pct = float(input())
pot = float(input())
N = float(input())

rot = Decimal(pot*(1-pct) + (pct*2/N))
ans = round(rot,6)
print (ans)


"""
According to the Theorem of Total Probability,
P(reach on time) = P(reach on time/ no car trouble) * P(no car trouble) + P(reach on time/ car trouble) * P(car trouble)
P(reach on time) = pot * (1 - pct) + (2/N) * pct
P(reach on time) = 0.3 * 0.8 + 0.2 * 0.2 = 0.24 + 0.04 = 0.28
"""