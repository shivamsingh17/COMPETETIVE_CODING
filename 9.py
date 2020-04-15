"""
Motu is playing a game. In this game he has given N boxes. First box contains exactly P ball(s) and last box contains exactly Q ball(s). He needs to fill the rest boxes with the following conditions :

a) Each box contain balls between 1 to K (inclusive)

b) Adjacent boxes must contain distinct number of balls

As Motu is only good in eating, so he is not able to find the number of ways to fill the boxes. Help him in calculating the number of ways to fill the boxes with given conditions. You are given N, K, P, Q.

Input:
-The first line of input contain a single integer T denoting the number of test cases.

-For each test case there are four space-separated integers N, K ,P and Q.

Output:
For each testcase, output in a single line , the number of ways to fill the boxes modulo 1000000007.

Constraints
1≤T≤100
3≤N≤105
2≤K≤105
1≤P≤K
1≤Q≤K
Sample Input:
1
4 3 2 3

Sample Output:
3

"""
def sol_dp(n, k, p, q):
    MOD = 1000000007
    nq = 1 if p == q else 0  # nb finishing by q
    noq = 0 if p == q else 1  # nb NOT finishing by q
    for _ in range(n - 1):
        nq, noq = noq, ((k - 1) * nq + (k - 2) * noq) % MOD
    return nq


def main():
    T = int(input())
    for i in range(T):
        n, k, p, q = map(int, input().split())
        print(sol_dp(n, k, p, q))


if __name__ == '__main__':
    main()