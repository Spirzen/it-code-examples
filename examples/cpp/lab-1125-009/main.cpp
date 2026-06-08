#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <numeric>

using namespace std;

using ll = long long;
const ll INF = (1LL << 60);
const int MOD = 1'000'000'007;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a) cin >> x;
    cout << accumulate(a.begin a.end 0LL) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t = 1;
    // cin >> t;   // раскомментируйте, если в условии несколько тестов
    while (t--) {
        solve();
    }
    return 0;
}
