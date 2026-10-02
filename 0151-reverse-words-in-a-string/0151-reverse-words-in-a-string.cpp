class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        vector<string> words;
        string word;

        // Extract words
        while (ss >> word) {
            words.push_back(word);
        }

        // Build answer in reverse order
        string result;

        for (int i = words.size() - 1; i >= 0; i--) {
            result += words[i];

            if (i != 0)
                result += " ";
        }

        return result;
    }
};