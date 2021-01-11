# -*- coding: utf-8 -*-
"""
Given four integers  and . Determine if there exists a binary string having  0's and  1's such that the total number of subsequences equal to the sequence "01" in it is  and the total number of subsequences equal to the sequence "10" in it is .

A binary string is a string made of the characters '0' and '1' only.

A sequence  is a subsequence of a sequence  if  can be obtained from  by deletion of several (possibly, zero or all) elements.

Input Format

The first line contains a single integer  (), denoting the number of test cases.

Each of the next  lines contains four integers , ,  and  ((, ()), as described in the problem.

Output Format

For each test case, output "Yes'' (without quotes) if a string with given conditions exists and "No'' (without quotes) otherwise.

SAMPLE INPUT 
3
3 2 4 2
3 3 6 3
3 3 4 3
SAMPLE OUTPUT 
Yes
Yes
No
Explanation
When x, y, a and b are 3, 2, 4 and 2 respectively, string 00110 is a valid string. So answer is Yes

When x, y, a and b are 3, 3, 4 and 3 respectively, we can't find any valid string. So answer is No.

@author: Aabha
"""

import sys
ip=sys.stdin.read()
 
for i in ip.split('\n'):
    stri=i.split()
    if (len(stri)!=4):
        print("")
    else:
        x,y,a,b=stri
        if(int(x)*int(y)==int(a)+int(b)):
            print("Yes")
        else:
            print("No")