class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # 1. Factorize t into powers of 2, 3, 5, 7
        req_a = req_b = req_c = req_d = 0
        temp_t = t
        for p, var in [(2, 'a'), (3, 'b'), (5, 'c'), (7, 'd')]:
            while temp_t % p == 0:
                if p == 2: req_a += 1
                elif p == 3: req_b += 1
                elif p == 5: req_c += 1
                elif p == 7: req_d += 1
                temp_t //= p
                
        if temp_t > 1:
            return "-1"
            
        # 2. Build DP table for (twos, threes)
        MAX_A, MAX_B = 60, 60
        dp = [[None] * MAX_B for _ in range(MAX_A)]
        dp[0][0] = (0, 0, 0, 0, 0, 0)  # counts for (2, 3, 4, 6, 8, 9)

        digits_info = [
            (2, 1, 0), (3, 0, 1), (4, 2, 0),
            (6, 1, 1), (8, 3, 0), (9, 0, 2)
        ]

        for i in range(MAX_A):
            for j in range(MAX_B):
                if i == 0 and j == 0:
                    continue
                best_tup, best_key = None, None
                for d, twos, threes in digits_info:
                    pi, pj = max(0, i - twos), max(0, j - threes)
                    
                    # Prevent self-loop / uninitialized access
                    if pi == i and pj == j:
                        continue
                        
                    prev = dp[pi][pj]
                    if prev is None:
                        continue
                        
                    c2, c3, c4, c6, c8, c9 = prev
                    if d == 2: c2 += 1
                    elif d == 3: c3 += 1
                    elif d == 4: c4 += 1
                    elif d == 6: c6 += 1
                    elif d == 8: c8 += 1
                    elif d == 9: c9 += 1
                    
                    new_tup = (c2, c3, c4, c6, c8, c9)
                    L = sum(new_tup)
                    S = '2'*c2 + '3'*c3 + '4'*c4 + '6'*c6 + '8'*c8 + '9'*c9
                    key = (L, S)
                    
                    if best_key is None or key < best_key:
                        best_key = key
                        best_tup = new_tup
                dp[i][j] = best_tup

        N = len(num)

        def digit_factors(d_int):
            if d_int == 0: return (0, 0, 0, 0)
            a = b = c = d_fact = 0
            val = d_int
            while val % 2 == 0: a += 1; val //= 2
            while val % 3 == 0: b += 1; val //= 3
            while val % 5 == 0: c += 1; val //= 5
            while val % 7 == 0: d_fact += 1; val //= 7
            return (a, b, c, d_fact)

        # 3. Compute prefix factor sums for num
        pref_a, pref_b = [0] * (N + 1), [0] * (N + 1)
        pref_c, pref_d = [0] * (N + 1), [0] * (N + 1)
        
        first_zero = N
        for idx, ch in enumerate(num):
            if ch == '0' and first_zero == N:
                first_zero = idx
            fa, fb, fc, fd = digit_factors(int(ch))
            pref_a[idx + 1] = pref_a[idx] + fa
            pref_b[idx + 1] = pref_b[idx] + fb
            pref_c[idx + 1] = pref_c[idx] + fc
            pref_d[idx + 1] = pref_d[idx] + fd

        # 4. Try matching length N candidates
        max_p = min(N, first_zero)
        for p in range(max_p, -1, -1):
            if p == N:
                # num itself is zero-free
                if (pref_a[N] >= req_a and pref_b[N] >= req_b and 
                    pref_c[N] >= req_c and pref_d[N] >= req_d):
                    return num
                continue
            
            rem_a = max(0, req_a - pref_a[p])
            rem_b = max(0, req_b - pref_b[p])
            rem_c = max(0, req_c - pref_c[p])
            rem_d = max(0, req_d - pref_d[p])
            
            start_digit = int(num[p]) + 1
            for d_int in range(start_digit, 10):
                fa, fb, fc, fd = digit_factors(d_int)
                rem2_a, rem2_b = max(0, rem_a - fa), max(0, rem_b - fb)
                rem2_c, rem2_d = max(0, rem_c - fc), max(0, rem_d - fd)
                
                c2, c3, c4, c6, c8, c9 = dp[rem2_a][rem2_b]
                L = (c2 + c3 + c4 + c6 + c8 + c9) + rem2_c + rem2_d
                rem_len = N - 1 - p
                
                if L <= rem_len:
                    ones_count = rem_len - L
                    suffix = (
                        '1' * ones_count +
                        '2' * c2 + '3' * c3 + '4' * c4 +
                        '5' * rem2_c + '6' * c6 +
                        '7' * rem2_d + '8' * c8 + '9' * c9
                    )
                    return num[:p] + str(d_int) + suffix

        # 5. Length > N candidate
        c2, c3, c4, c6, c8, c9 = dp[req_a][req_b]
        L_min = (c2 + c3 + c4 + c6 + c8 + c9) + req_c + req_d
        len_ans = max(N + 1, L_min)
        
        ones_count = len_ans - L_min
        return (
            '1' * ones_count +
            '2' * c2 + '3' * c3 + '4' * c4 +
            '5' * req_c + '6' * c6 +
            '7' * req_d + '8' * c8 + '9' * c9
        )