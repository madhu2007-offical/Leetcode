class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastIndex;
        int left = 0, ans = 0;

        for (int right = 0; right < s.size(); right++) {
            if (lastIndex.count(s[right]) && lastIndex[s[right]] >= left) {
                left = lastIndex[s[right]] + 1;
            }
            lastIndex[s[right]] = right;
            ans = max(ans, right - left + 1);
        }

        return ans;
    }
};