class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int ans = 0;

        for (int j = 0; j < n; j++) {
            int leftSmaller = 0, leftGreater = 0;
            int rightSmaller = 0, rightGreater = 0;

            for (int i = 0; i < j; i++) {
                if (rating[i] < rating[j])
                    leftSmaller++;
                else
                    leftGreater++;
            }

            for (int k = j + 1; k < n; k++) {
                if (rating[k] > rating[j])
                    rightGreater++;
                else
                    rightSmaller++;
            }

            ans += leftSmaller * rightGreater;
            ans += leftGreater * rightSmaller;
        }

        return ans;
    }
};