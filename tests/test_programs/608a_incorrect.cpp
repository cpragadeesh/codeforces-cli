#include <iostream>
#include <algorithm>

#define ll long long
#define debug(x) cout<<#x<<": "<<x<<endl

using namespace std;

ll f[1010], t[1010];

int main() {

  ll n, s;
  cin>>n>>s;

  ll ans = 0;

  for(int i = 0; i < n; i++) {
    ll a, b;
    cin>>a>>b;
    f[a] = 1;
    t[a] = max(b, t[a]);
  }

  for(int i = s; i >= 0; i--, ans++) {
    if(f[i] == 1 and t[i] > ans)
      ans = t[i];
  }

  ans--;
  cout<<ans - 1<<endl;

  return 0;
}
