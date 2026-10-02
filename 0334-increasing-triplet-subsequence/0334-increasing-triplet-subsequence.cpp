class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX;
        int second = INT_MAX;

        for (int num : nums) {
            
            // Smallest value seen so far
            if (num <= first) {
                first = num;
            }
            
            // Smallest possible second value
            else if (num <= second) {
                second = num;
            }
            
            // num > first && num > second
            else {
                return true;
            }
        }

        return false;
    }
};