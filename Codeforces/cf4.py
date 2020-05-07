t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    freq = [0 for i in range(2*k+5)]
    freq2 = [0 for i in range(2*k+5)]
    def check(ans1):
        ans = float('inf')
        best = 0
        for i in range(1, (2*k)+5):
            tmp = 0
            for j in range(n//2):
                if (a[j] + a[n-j-1] != i):
                    if (i-a[j] >= 1 and i - a[j] <= k):
                        tmp += 1
                    elif (i-a[n-j-1] >= 1 and i-a[n-j-1] <= k):
                        tmp += 1
                    else:
                        tmp += 2
            if (tmp < ans):
                best= i
            ans = min(ans, tmp)
        return ans
    for i in range(n//2):
        freq[min(a[n-1-i], a[i])+1] -= 1
        freq[0] += 1
        freq[max(a[n-1-i], a[i])+k+1] += 1
    for i in range(n//2):
        freq2[a[i] + a[n-i-1]] +=1
    ans = float('inf')
    for i in range(1, 2 * k + 1):
        freq[i] += freq[i-1]
        ans = min(ans, freq[i] + n//2 - freq2[i])
    print(ans)
	
	
	#include<bits/stdc++.h>
#define pii pair<int,int>
#define ll long long
#define cl(x,y) memset(x,y,sizeof(x))
#define ct cerr<<"Time elapsed:"<<1.0*clock()/CLOCKS_PER_SEC<<"s.\n";
const int N=4e5+10;
const int mod=1e9+7;
const int inf=0x3f3f3f3f;
using namespace std;
int a[N],b[N]={0};
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	while(t--)
	{
		int n,k,i;
		cin>>n>>k;
		for(i=1;i<=n;i++)
			cin>>a[i];
		for(i=1;i<=n/2;i++)
		{
			int sum=a[i]+a[n-i+1],m1,m2;
			m1=min(a[i],a[n-i+1]);
			m2=max(a[i],a[n-i+1]);
			b[1]+=2;
			b[2*k+1]-=2;
			b[m1+1]--;
			b[m2+k+1]++;
			b[sum]--;
			b[sum+1]++;
		}
		int ans=inf;
		for(i=1;i<=2*k;i++)
		{
			b[i]+=b[i-1];
			ans=min(ans,b[i]);
		}
		cout<<ans<<endl;
		for(i=1;i<=2*k+1;i++)
			b[i]=0;
	}
	return 0;
}




import sys
input=sys.stdin.readline
from collections import deque
t=int(input())
def inc(n,arr,l,r):
    if(l<=r and l>=0):
        arr[l]+=n
        if(r+1<=len(arr)-1):
            arr[r+1]-=n


for i1 in range(t):
    n,k=list(map(int,input().split(" ")))
    l1=list(map(int,input().split(" ")))
    arr=[0]*(2*k+1)
    for i in range(n//2):
        z1=l1[i]
        z2=l1[n-i-1]
        s=z1+z2
        min1=min(z1,z2)
        max1=max(z1,z2)
        if(s!=2*k):
            l,r=s+k-min1+1,2*k
            inc(2,arr,l,r)
            
            l,r=s+1,s+k-min1
            inc(1,arr,l,r)

        l,r=s-(max1-1),s-1  
        inc(1,arr,l,r)

        l,r=0,s-(max1-1)-1 
        inc(2,arr,l,r) 
    for i in range(1,len(arr)):
        arr[i]+=arr[i-1]
    # print(arr)
    print(min(arr))


