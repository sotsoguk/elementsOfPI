#include <iostream>
#include <queue>
#include <cstdlib>
#include <vector>

using namespace std;

template<typename T> void print_queue(T q) {
    while(!q.empty()) {
        std::cout << q.top() << " ";
        q.pop();
    }
    std::cout << '\n';
}
struct heap_entry{
    size_t idx;
    int value;
};
struct CompareHeapentry{
    bool operator()(const heap_entry& lhs, const heap_entry& rhs)
    {
        return lhs.value > rhs.value;
    }
};

std::ostream& operator<< (std::ostream& o, const heap_entry& h)
{
    o << h.value<<",";
    return o;
}

std::vector<int> merge_sorted_arrays(std::vector<std::vector<int>>& sorted_arrays){
  
    std::priority_queue<heap_entry, std::vector<heap_entry>, CompareHeapentry> min_heap;
    std::vector<int> result;
    size_t numArrays = sorted_arrays.size();
    std::vector<int> idxs (sorted_arrays.size(),0);
    
    // std::vector<std::vector<int>::iterator> iterators;
    // // put the first element of each array into the heap
    // for (size_t i= 0;i<numArrays;i++){
    //     cout << i <<"\t";
    //     if (iterators.at(i) != sorted_arrays.at(i).end()){
    //         min_heap.push( heap_entry{i,*(iterators.at(i))} );
    //     }
    //     iterators.at(i)++;
    // }
    // // cout << "Here";
    // // print_queue(min_heap);
    for (size_t i=0;i<numArrays;i++){
        if (idxs.at(i) < sorted_arrays.at(i).size()){
            min_heap.push(heap_entry{i,sorted_arrays.at(i).at(idxs.at(i))});
        }
        idxs.at(i)++;
    }
    while (!min_heap.empty()) {
        heap_entry smallest = min_heap.top();
        min_heap.pop();
        result.push_back(smallest.value);
        size_t nextIndex = smallest.idx;
        if (idxs[nextIndex]<sorted_arrays.at(nextIndex).size()){
            min_heap.push(heap_entry{nextIndex,sorted_arrays.at(nextIndex).at(idxs.at(nextIndex))});
            idxs.at(nextIndex)++;
        }

    }


    print_queue(min_heap);
    return result;
}
int main(int argc, char const *argv[])
{
    /* code */
    
    // srand(42);
    // size_t nums = 10;
    // size_t maxNum = 100;
    // std::vector<int> array(nums,0);
    // for (auto it = array.begin();it != array.end();it++){
    //     *it = rand() % maxNum;
    // }
    // for (auto it = array.begin();it != array.end();it++){
    //     std::cout << *it << ",";
    // }
    // std::cout << std::endl;
    // std::priority_queue<int> q;
    // for (auto i:array) {
    //     q.push(i);
    // }
    // print_queue(q);
    // print_queue(q);
    // return 0;
    std::vector<int> a = {1,5,10};
    std::vector<int> b = {2,6,11};
    std::vector<int> c = {3,7,12};
    //std::vector<std::vector<int>> as {{1,5,10},{2,6,11},{3,7,12}};
    std::vector<std::vector<int>> as {a,b,c};
    cout << "Hello";
    std::vector<int> result = merge_sorted_arrays(as);
    for (auto i:result){
        cout << i <<",";
    }
}
