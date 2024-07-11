impl Solution {
    pub fn two_egg_drop(n: i32) -> i32 {
        let mut dp = vec![vec![0; n as usize + 1]; 3];
        for m in 1..=n as usize {
            dp[1][m] = m;
        }

        for m in 1..=n as usize {
            dp[2][m] = m;
            for x in 1..=m {
                dp[2][m] = dp[2][m].min(1 + dp[1][x-1].max(dp[2][m-x]));
            }
        }

        dp[2][n as usize].try_into().unwrap()
    }
}