class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size();
        const int INF = n + 1;

        // best[i] = minimum length of a valid subarray
        // completely inside arr[0 ... i-1]
        vector<int> best(n + 1, INF);

        int left = 0;
        int sum = 0;
        int answer = INF;

        for (int right = 0; right < n; right++) {
            sum += arr[right];

            // Since all elements are positive,
            // shrink the window if sum becomes too large.
            while (sum > target) {
                sum -= arr[left];
                left++;
            }

            if (sum == target) {
                int length = right - left + 1;

                // Find the shortest valid subarray
                // that ends before 'left'.
                if (best[left] != INF) {
                    answer = min(answer, length + best[left]);
                }

                // Current subarray can be the best
                // valid subarray for this prefix.
                best[right + 1] = min(best[right], length);
            } 
            else {
                best[right + 1] = best[right];
            }
        }

        return answer == INF ? -1 : answer;
    }
};