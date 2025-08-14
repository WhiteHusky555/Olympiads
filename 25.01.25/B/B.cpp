

#include <iostream>
#include <string>
int main()
{   
    int x;
    std::cin >> x;
    int count = 0;
    for (int i = 0; i <= x ; i+=10) {
        if (i == 0 or i % 10 == 0 or i == x) {
            count += std::to_string(i).length();
        };
    };
    if (x % 10 != 0) {
        count += std::to_string(x).length();
    };
    std::cout << count;
}

