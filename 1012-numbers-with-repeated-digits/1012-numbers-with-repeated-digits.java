class Solution {
    public int numDupDigitsAtMostN(int n) {
        String s = String.valueOf(n);
        int len = s.length();

        // Count numbers with fewer digits than n
        int unique = 0;

        for (int digits = 1; digits < len; digits++) {
            // First digit: 9 choices (1-9)
            // Remaining digits: 9, 8, 7... choices
            int count = 9;

            for (int j = 1; j < digits; j++) {
                count *= (10 - j);
            }

            unique += count;
        }

        // Count numbers having same number of digits as n
        int mask = 0;

        for (int i = 0; i < len; i++) {
            int digit = s.charAt(i) - '0';

            // Digits smaller than current digit
            // that haven't been used yet
            int smaller = 0;

            for (int d = (i == 0 ? 1 : 0); d < digit; d++) {
                if ((mask & (1 << d)) == 0) {
                    smaller++;
                }
            }

            // Number of ways to fill remaining positions
            int remaining = len - i - 1;
            int permutations = 1;

            for (int j = 0; j < remaining; j++) {
                permutations *= (9 - i - j);
            }

            unique += smaller * permutations;

            // If current digit is already used,
            // n itself and all following possibilities
            // cannot continue as unique.
            if ((mask & (1 << digit)) != 0) {
                break;
            }

            mask |= (1 << digit);

            // If this is the last digit, n itself is unique
            if (i == len - 1) {
                unique++;
            }
        }

        return n - unique;
    }
}