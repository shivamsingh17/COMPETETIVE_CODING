Given an array arr of size n containing only distinct integers, you need to find total times you see a series of consecutive integers of length greater than 1.
A series of consecutive integers is defined as arr[i], arr[i]+1, arr[i]+2...and so on.

Input:
The first line of input contains T denoting the numbers of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains the size of array n. The second line contains the elements of the array.

Output:
For each testcase, in a newline, print the total times you see a series of consecutive numbers.

Constraints:
1 <= T <= 100
1 <= n <= 103
0 <= arri <= 107

Examples:
Input:
3
7
5 7 9 10 11 13 14
6
0 1 2 4 5 7
7
1 0 2 9 3 8 6
Output:
2
2
0

Explanation:
Testcase1: The array is {5 7 9 10 11 13 14}. Here, 9 10 11 is one series of consecutive integers with length greater than 1. Again, 13 14 is another series of consecutive integers with length greater than 1. So, a total of two times we see such a series. Hence the answer is 2.

 


 
 for t in range(int(input())):
    N=int(input())
    l = list(map(int,input().split()))
    c = 0
    
    i=0
    j=i+1
    while i<N:
        j=i+1
        while j<N:
            if l[j]!=l[j-1]+1:
                break
            j+=1
        if j-i>1:
            c += 1
        i=j
    print(c)
                
        