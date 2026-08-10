#include <stdbool.h>
#include <math.h>

bool winnerSquareGame(int n) {

    bool dp[n + 1];

    dp[0] = false;

    for (int i = 1; i <= n; i++) {

        dp[i] = false;

        for (int j = 1; j * j <= i; j++) {

            int square = j * j;

            if (dp[i - square] == false) {
                dp[i] = true;
                break;
            }
        }
    }

    return dp[n];
}