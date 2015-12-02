"""
On a positive integer, you can perform any one of the following 3 steps. 
1.) Subtract 1 from it. (n = n-1), 
2.) If its divisible by 2, divide by 2. (if n % 2 == 0 , then n = n/2), 
3.) If its divisible by 3, divide by 3. (if n % 3 == 0 , then n = n/3). 
Now the question is, given a positive integer n, find the minimum number of 
steps that takes n to 1.
eg: 1.) For n = 1 , output: 0
    2.) For n = 4 , output: 2  (4/2 = 2/2 = 1)    
    3.) For n = 7 , output: 3  (7-1 = 6/3 = 2/2 = 1)
    4.) For n = 10, output: 3  (10-1 = 9/3 = 3/3 = 1) 
"""

def getMinSteps (n):
    dp = [0] * (n+1)  # initialize array of size n+1
    for i in range(2, n+1):
        dp[i] = 1 + dp[i-1]
        if i % 2 == 0: 
        	dp[i] = min(dp[i], 1+dp[i/2])
        if i % 3 == 0: 
        	dp[i] = min(dp[i], 1+dp[i/3])
    return dp

print getMinSteps(10)


[0,0,0,0,0,0,0,0,0]
[0,0,1,0,0,0,0,0,0]