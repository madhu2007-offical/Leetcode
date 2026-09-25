class Solution {
public:
    using Set = set<string>;

    string s;
    int i = 0;

    // Parse an expression until ',' or '}'
    Set parseExpression() {
        Set result = parseTerm();

        while (i < s.size() && s[i] == ',') {
            i++; // skip ','
            Set next = parseTerm();

            result.insert(next.begin(), next.end());
        }

        return result;
    }

    // Parse concatenated terms
    Set parseTerm() {
        Set result = {""};

        while (i < s.size() && s[i] != '}' && s[i] != ',') {
            Set part;

            if (s[i] == '{') {
                i++; // skip '{'

                part = parseExpression();

                i++; // skip '}'
            }
            else {
                // Single lowercase letter
                part.insert(string(1, s[i]));
                i++;
            }

            // Cartesian product = concatenation
            Set temp;

            for (const string& a : result) {
                for (const string& b : part) {
                    temp.insert(a + b);
                }
            }

            result = move(temp);
        }

        return result;
    }

    vector<string> braceExpansionII(string expression) {
        s = expression;
        i = 0;

        Set result = parseExpression();

        return vector<string>(result.begin(), result.end());
    }
};