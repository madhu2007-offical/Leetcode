class Solution {
public:
    bool checkValidString(string s) {
        int low = 0;
        int high = 0;

        for (char c : s) {
            if (c == '(') {
                low++;
                high++;
            }
            else if (c == ')') {
                low--;
                high--;
            }
            else { // '*'
                low--;      // '*' acts as ')'
                high++;     // '*' acts as '('
            }

            // Even the maximum possible '(' count is negative
            if (high < 0)
                return false;

            // We cannot have negative unmatched '('
            low = max(low, 0);
        }

        // If zero unmatched '(' is possible, string is valid
        return low == 0;
    }
};