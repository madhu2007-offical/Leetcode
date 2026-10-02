class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;

        int maxCandies = 0;

        // Find the maximum candies any kid currently has
        for (int candy : candies) {
            maxCandies = max(maxCandies, candy);
        }

        // Check each kid after giving extra candies
        for (int candy : candies) {
            result.push_back(candy + extraCandies >= maxCandies);
        }

        return result;
    }
};