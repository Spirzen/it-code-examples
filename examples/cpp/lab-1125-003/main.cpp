int t;
cin >> t;
while (t--) {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &x : a) {
        cin >> x;
    }
    long long sum = 0;
    for (int x : a) {
        sum += x;
    }
    cout << sum << '\n';
}
