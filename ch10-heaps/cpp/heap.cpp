#include <iostream>
#include <queue>
#include <cstdlib>
#include <vector>

using namespace std;

template<typename T> void print_queue(T& q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}

int main(int argc, char const *argv[])
{
    /* code */
    
    srand(42);
    size_t nums = 10;
    size_t maxNum = 100;
    std::vector<int> array(nums,0);
    for (auto it = array.begin();it != array.end();it++){
        *it = rand() % maxNum;
    }
    for (auto it = array.begin();it != array.end();it++){
        std::cout << *it << ",";
    }
    std::cout << std::endl;
    std::priority_queue<int> q;
    for (auto i:array) {
        q.push(i);
    }
    print_queue(q);
    return 0;
}
