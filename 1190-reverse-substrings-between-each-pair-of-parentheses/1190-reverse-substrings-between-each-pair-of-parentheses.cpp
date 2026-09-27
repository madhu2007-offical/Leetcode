class Solution {
public:
    string reverseParentheses(string s) {
        stack<string> st;
        st.push("");

        for (char c : s) {
            if (c == '(') {
                st.push("");
            }
            else if (c == ')') {
                string cur = st.top();
                st.pop();

                reverse(cur.begin(), cur.end());

                st.top() += cur;
            }
            else {
                st.top() += c;
            }
        }

        return st.top();
    }
};