vector<int> a = {1, 2, 3, 4, 6};
int target = 6;
int l = 0, r = (int)a.size() - 1;
while (l < r) {
  int s = a[l] + a[r];
  if (s == target) {
    cout << l << " " << r << '\n';
    break;
  }
  if (s < target) {
    ++l;
  } else {
    --r;
  }
}
