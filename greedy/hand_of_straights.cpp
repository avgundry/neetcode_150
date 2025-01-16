#include <iostream>
#include <map>
#include <vector>
class Solution {
public:
    bool isNStraightHand(std::vector<int>& hand, int groupSize) {
        // First, check if the hand is actually evenly divisible into groups of size groupSize.
        // If not, return False immediately.
        int n = hand.size();
        if (n == 0 or n % groupSize != 0) {
            return false;
        }

        // Build a dictionary counting each element.
        std::map<int, int> cards;
        for (auto i = hand.begin(); i != hand.end(); ++i) {
            // If the card already is in the map, just add to it.
            if (cards.count(*i) == 1) {
                cards[*i] += 1;
            } else {
                cards[*i] = 1;
            }
        }

        // While the dictionary still has elements, create a group out of it until 
        // we reach the groupsize.
        while (cards.size() > 0) {
            int curr_size = 1;
            int curr = cards.begin()->first;

            while (curr_size < groupSize) {
                auto next = cards.find(curr + 1);
                // If the card isn't found, return false
                if (next == cards.end()) {
                    return false;
                } else {
                    cards[curr + 1] -= 1;
                    if (cards[curr + 1] == 0) {
                        cards.erase(curr + 1);
                    }
                    curr += 1;
                    curr_size += 1;
                }
            }
        }

        return true;
    }
};

int main() {
    Solution solution;

    std::vector<int> hand1 = {1, 2, 3};
    int groupSize1 = 1;

    std::cout << "Test case 1 result: " << (solution.isNStraightHand(hand1, groupSize1)) << std::endl;
}

        // BRUTE FORCE APPROACH
        // While we still have cards left in hand:
        // while (hand.size() > 0) {
        //     // build a group out of them. 
        //     std::vector<int> group;
        //     // Begin with a group of the last element, which we call curr.
        //     // Remove it as we go.
        //     int curr = hand.back();
        //     group.push_back(curr);
        //     hand.pop_back();
        //     int target = -1;

        //     while (group.size() < groupSize) {
        //         // Then search backwards for an element curr - 1 in hand.
        //         reverse_itre(std::vector) i = hand.rbegin();
        //         auto start= hand.rend();
        //         for (i; i != start; ++i) {
        //             // If it exists, pop it, and make it the new curr, until our 
        //             // group is of size groupSize.
        //             if (*i == curr - 1) {
        //                 curr = *i;
        //                 group.push_back(curr);
        //                 // Erase it from the list. (Have to call extra functions since it's a reverse iter...)
        //                 hand.erase(std::next(i).base());
        //                 break;
        //             }
        //         }
        //         // If no such element is found, return False.
        //         if (i == hand.rend()) {
        //             return false;
        //         }
        //     }

        // }

        // // If we have removed all cards from hand, return True.
        // return true;
    // }
