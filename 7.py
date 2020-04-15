"""
Patlu has recently got a new problem based on Pallindromes. A Pallindrome is a number that is same from front and back, example 121 is pallindrome but 123 is not . He wants to calculate sum of all N digit number which are Pallindromic in nature and divisible by 9 and does not contain any zero in their decimal representation. As the answer can be very large so print the sum modulo 109+7.

Input:
First line of input contain T, number of testcases. Then the testcases follow.
Each testcase contains single line of input , one integer N.
Output:
For each testcase, output in a single line answer having N digits pallindromic string.
Constraints
1≤T≤100
1≤N≤105
Sample Input:
  2
  1
  2
Sample Output:
  9
  99
  
 """

def getsum(N):
	if N==1:
		return 9
	if N==2:
		return 99
	s = ""
	for i in range(0,N):
		s = s+'5'
	s = int(s)
	if N%2==0:
		s = s*pow(9,N//2-1)
	else:
		s = s*pow(9,N//2)
	return s%(pow(10,9)+7)

def main():
	t = int(input())
	for _ in range(0,t):
		N = int(input())
		result = getsum(N)
		print(result)
if __name__ == "__main__":
	main()
