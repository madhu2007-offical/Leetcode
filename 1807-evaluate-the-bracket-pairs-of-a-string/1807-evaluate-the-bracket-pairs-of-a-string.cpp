
class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> mp;

        // Store key-value pairs
        for (auto &pair : knowledge) {
            mp[pair[0]] = pair[1];
        }

        string ans;

        for (int i = 0; i < s.size(); i++) {

            if (s[i] != '(') {
                ans += s[i];
            } 
            else {
                // Find closing bracket
                int j = i + 1;

                while (s[j] != ')') {
                    j++;
                }

                // Extract key
                string key = s.substr(i + 1, j - i - 1);

                // Replace bracket pair
                if (mp.count(key)) {
                    ans += mp[key];
                } else {
                    ans += '?';
                }

                // Skip to character after ')'
                i = j;
            }
        }

        return ans;
    }
};

