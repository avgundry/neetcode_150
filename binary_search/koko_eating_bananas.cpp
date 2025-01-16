#include <iostream>
#include <vector>

class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        // Not possible to eat them all in time in this case.
        return 0;
        // if ((piles).size() > h) {
        //     return -1;
        // }
        // return 0;
    }
};

int main() {
    Solution s = Solution();
    std::vector<int> piles1 = {3,6,7,11};
    std::vector<int> piles2 = {30,11,23,4,20};
    int h1 = 8;
    int h2 = 5;
    int h3 = 6;
    std::cout << "piles1: ";
    for (auto i = 0; i < piles1.size(); ++i) {
        std::cout << piles1[i] << ", ";
    }
    std::cout << ", h1: " << h1 << "; output: " << s.minEatingSpeed(piles1, h1);
}