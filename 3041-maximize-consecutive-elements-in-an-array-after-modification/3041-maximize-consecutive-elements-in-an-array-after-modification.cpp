#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        // Max value in nums is 10^6, so max modified value is 10^6 + 1
        int max_val = nums.back() + 2;
        vector<int> dp(max_val, 0);
        int ans = 0;
        
        for (int x : nums) {
            dp[x + 1] = dp[x] + 1;
            dp[x] = dp[x - 1] + 1;
            ans = max({ans, dp[x], dp[x + 1]});
        }
        
        return ans;
    }
};