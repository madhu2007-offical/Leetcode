class Solution {
public:
    struct State {
        long long score = 0;
        vector<int> ids;
    };

    bool better(const State& a, const State& b) {
        if (a.score != b.score)
            return a.score > b.score;

        return a.ids < b.ids;
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // {left, right, weight, original index}
        vector<array<long long, 4>> a;

        for (int i = 0; i < n; i++) {
            a.push_back({
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            });
        }

        // Sort by right endpoint.
        sort(a.begin(), a.end(), [](auto& x, auto& y) {
            if (x[1] != y[1])
                return x[1] < y[1];
            return x[0] < y[0];
        });

        // Ends of intervals.
        vector<long long> ends(n);

        for (int i = 0; i < n; i++)
            ends[i] = a[i][1];

        /*
            prev[i] = number of intervals among [0 ... i-1]
                       whose right endpoint < a[i].left

            We use lower_bound(left) because we need:
                right < left
        */
        vector<int> prev(n);

        for (int i = 0; i < n; i++) {
            prev[i] =
                lower_bound(ends.begin(), ends.begin() + i, a[i][0])
                - ends.begin();
        }

        /*
            dp[i][k]:
            best answer using first i sorted intervals
            with at most k chosen intervals.

            We only need k = 0..4.
        */
        vector<array<State, 5>> dp(n + 1);

        for (int i = 1; i <= n; i++) {
            int idx = i - 1;

            for (int k = 0; k <= 4; k++) {

                // Option 1: don't choose current interval.
                dp[i][k] = dp[i - 1][k];

                // Option 2: choose current interval.
                if (k > 0) {
                    State candidate =
                        dp[prev[idx]][k - 1];

                    candidate.score += a[idx][2];

                    // Insert original index and keep IDs sorted.
                    candidate.ids.push_back((int)a[idx][3]);
                    sort(candidate.ids.begin(), candidate.ids.end());

                    if (better(candidate, dp[i][k])) {
                        dp[i][k] = candidate;
                    }
                }
            }
        }

        return dp[n][4].ids;
    }
};