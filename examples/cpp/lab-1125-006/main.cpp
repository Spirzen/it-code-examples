void dfs(int v, const vector<vector<int>> &g, vector<bool> &used) {
    used[v] = true;
    for (int to : g[v]) {
        if (!used[to]) {
            dfs(to, g, used);
        }
    }
}

// запуск обхода всего графа
vector<bool> used(n);
for (int i = 0; i < n; ++i) {
    if (!used[i]) {
        dfs(i, g, used);
    }
}
