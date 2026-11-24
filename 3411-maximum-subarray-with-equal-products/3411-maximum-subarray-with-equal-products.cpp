class Solution {
public:
    int maxLength(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            long long prod = 1;
            long long g = 0, l = 1;

            for (int j = i; j < n; j++) {
                g = gcd(g, (long long)nums[j]);
                l = lcm(l, (long long)nums[j]);

                if (prod > LLONG_MAX / nums[j])
                    break;

                prod *= nums[j];

                if (prod == g * l) {
                    ans = max(ans, j - i + 1);
                }

                if (prod > g * l)
                    break;
            }
        }

        return ans;
    }
};