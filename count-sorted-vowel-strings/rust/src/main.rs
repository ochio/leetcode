impl Solution {
    pub fn count_vowel_strings(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![[1; 5]; n];
        let mut s = 5;

        for i in 1..n {
            for j in 0..5 {
                if j == 0 {
                    dp[i][j] = s;
                } else {
                    dp[i][j] = dp[i][j-1] - dp[i-1][j-1];
                    s += dp[i][j];
                }
            }
        }
        s
    }
}