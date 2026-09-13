class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        int ans = 0;

        // Try every possible row and column shift
        for (int dr = -(n - 1); dr <= n - 1; dr++) {
            for (int dc = -(n - 1); dc <= n - 1; dc++) {

                int overlap = 0;

                for (int r = 0; r < n; r++) {
                    for (int c = 0; c < n; c++) {

                        int nr = r + dr;
                        int nc = c + dc;

                        // Check if shifted position is inside img2
                        if (nr >= 0 && nr < n &&
                            nc >= 0 && nc < n) {

                            if (img1[r][c] == 1 && img2[nr][nc] == 1) {
                                overlap++;
                            }
                        }
                    }
                }

                ans = max(ans, overlap);
            }
        }

        return ans;
    }
};