class Solution {
public:
    vector<string> ans;

    void backtrack(int index, string &digits, string &curr, vector<string> &mp) {
        if (index == digits.size()) {
            ans.push_back(curr);
            return;
        }

        string letters = mp[digits[index] - '0'];

        for (char ch : letters) {
            curr.push_back(ch);
            backtrack(index + 1, digits, curr, mp);
            curr.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> mp = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };

        string curr = "";
        backtrack(0, digits, curr, mp);

        return ans;
    }
};