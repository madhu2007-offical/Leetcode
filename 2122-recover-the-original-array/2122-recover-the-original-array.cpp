class Solution {
public:
    vector<int> recoverArray(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int n = nums.size() / 2;

        // Try every possible value of 2*k
        for (int i = 1; i < nums.size(); i++) {
            int diff = nums[i] - nums[0];

            // k must be positive and diff = 2*k
            if (diff <= 0 || diff % 2 != 0)
                continue;

            int k = diff / 2;

            map<int, int> freq;

            for (int x : nums)
                freq[x]++;

            vector<int> ans;
            bool valid = true;

            // Smallest remaining value must be a lower value.
            for (int j = 0; j < nums.size(); j++) {
                int x = nums[j];

                if (freq[x] == 0)
                    continue;

                // x = arr - k
                // x + 2k = arr + k
                if (freq[x + 2 * k] == 0) {
                    valid = false;
                    break;
                }

                freq[x]--;
                freq[x + 2 * k]--;

                ans.push_back(x + k);

                if (ans.size() == n)
                    break;
            }

            if (valid && ans.size() == n)
                return ans;
        }

        return {};
    }
};