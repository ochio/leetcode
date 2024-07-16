impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        let s = s.as_bytes();
        let n = s.len();
        let mut ans = 0;
        let mut dp = vec![vec![false;n];n];

        for i in 0..n {
            dp[i][i] = true;
            ans += 1;
        }

        for i in 0..n-1 {
            if s[i] == s[i+1] {
                dp[i][i+1] = true;
                ans += 1;
            }
        }

        for l in 3..=n {
            for i in 0..n-l+1 {
                let j = i + l - 1;
                if s[i] == s[j] && dp[i+1][j-1] {
                    dp[i][j] = true;
                    ans += 1;
                }
            }
        }

        ans
    }
}