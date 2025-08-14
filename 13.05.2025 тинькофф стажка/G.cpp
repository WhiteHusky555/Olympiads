#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

// Функция для получения всех пар (p, q), таких что p*q = a[i] и gcd(p, q) == 1
vector<pair<int, int>> getCoprimeFactors(int x) {
    vector<pair<int, int>> result;
    for (int i = 1; i * i <= x; ++i) {
        if (x % i == 0) {
            int j = x / i;
            if (__gcd(i, j) == 1) {
                result.emplace_back(i, j);
                if (i != j) {
                    result.emplace_back(j, i);
                }
            }
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n - 1);
    for (int &x : a) cin >> x;

    // map: текущая позиция &rarr; значение числа &rarr; сумма интересностей
    unordered_map<long long, long long> curr, next;

    // Инициализация: b[0]/b[1] = a[0]
    for (auto [p, q] : getCoprimeFactors(a[0])) {
        long long key = ((long long)p << 32) | q;
        curr[key] = (1LL * p * q) % MOD;
    }

    // Проход по всем позициям
    for (int i = 1; i < n - 1; ++i) {
        next.clear();
        for (auto &[key, val] : curr) {
            int prev_p = key >> 32;
            int prev_q = key & 0xFFFFFFFF;
            for (auto [p, q] : getCoprimeFactors(a[i])) {
                if (prev_q == p) {
                    long long new_key = ((long long)prev_p << 32) | q;
                    long long new_val = (val * 1LL * q) % MOD;
                    next[new_key] = (next[new_key] + new_val) % MOD;
                }
            }
        }
        swap(curr, next);
    }

    // Подсчёт окончательной суммы интересностей
    long long total = 0;
    for (auto &[key, val] : curr) {
        total = (total + val) % MOD;
    }

    cout << total << '\n';
    return 0;
}