"""
In these days of Lockdown, Motu's Father bussiness is in Loss. On Zeroth day of Lockdown the loss was Rs P, then Rs Q on the First day. Motu observed loss as a function and wanted to calculate the loss on Nth day of the Lockdown. He observed that the loss is dependent on the previous days, i.e. F(n)=F(n−1)+F(n−2)+F(n−1)∗F(n−2)
You are given the loss on Zeroth day and the First day of Lockdown. You have to find the loss on Nth day.
"""

mod = 10**9 + 7

def fib(n): 
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
          
    return F[0][0] 
      
def multiply(F, M): 
      
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0])%(mod-1)
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1])%(mod-1)
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0])%(mod-1)
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1])%(mod-1)
      
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 
          
# Optimized version of 
# power() in method 4  
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], 
         [1, 0]]; 
          
    power(F, n // 2) 
    multiply(F, F) 
          
    if (n % 2 != 0): 
        multiply(F, M) 

t = int(input())
for _ in range(t):
    p, q, n = map(int, input().split())
    if n == 0:
        print(p)
        continue
        
    f1 = fib(n)
    f2 = fib(n-1)
    ans = pow(p+1, f2, mod)*pow(q+1, f1, mod)
    ans -= 1
    ans %= mod

    print(ans)
