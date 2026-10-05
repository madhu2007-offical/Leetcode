class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;
        
        for (int a : asteroids) {
            bool destroyed = false;
            
            while (!st.empty() && st.back() > 0 && a < 0) {
                if (st.back() < -a) {
                    st.pop_back();        // stack asteroid explodes
                }
                else if (st.back() == -a) {
                    st.pop_back();        // both explode
                    destroyed = true;
                    break;
                }
                else {
                    destroyed = true;     // current explodes
                    break;
                }
            }
            
            if (!destroyed)
                st.push_back(a);
        }
        
        return st;
    }
};