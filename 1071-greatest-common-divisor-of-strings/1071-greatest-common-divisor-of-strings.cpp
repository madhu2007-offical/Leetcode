class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        // If they cannot be formed from the same repeating pattern
        if (str1 + str2 != str2 + str1) {
            return "";
        }

        // Length of the largest common repeating string
        int len = gcd(str1.size(), str2.size());

        return str1.substr(0, len);
    }
};