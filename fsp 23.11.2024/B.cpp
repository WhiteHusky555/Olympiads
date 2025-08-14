#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<long long> fibonacci(int n) {
    vector<long long> fib;
    fib.push_back(1);
    fib.push_back(1);
    for (int i = 2; i <= n; ++i) {
        fib.push_back(fib[i - 1] + fib[i - 2]);
    }
    return fib;
}

int countTriangles(int n) {
    vector<long long> fib = fibonacci(n);
    set<tuple<long long, long long, long long>> triangles;

    for (size_t i = 0; i < fib.size(); ++i) {
        for (size_t j = i; j < fib.size(); ++j) {
            for (size_t k = j; k < fib.size(); ++k) {
                long long a = fib[i], b = fib[j], c = fib[k];
                if (a + b > c) {
                    triangles.insert(make_tuple(a, b, c));
                }
            }
        }
    }
    return triangles.size();
}

int main() {
    int n;
    cin >> n;
    cout << countTriangles(n) << endl;
    return 0;
}
