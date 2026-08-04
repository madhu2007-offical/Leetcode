class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = n * n;

        int repeated = -1, missing = -1;

        for (int i = 1; i <= m; i++) {
            int count = 0;

            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r][c] == i)
                        count++;
                }
            }

            if (count == 2)
                repeated = i;
            else if (count == 0)
                missing = i;
        }

        return {repeated, missing};
    }
};