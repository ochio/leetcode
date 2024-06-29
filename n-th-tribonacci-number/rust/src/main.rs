impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut dp = vec![0, 1, 1];
        for i in 3..=n as usize {
            let v = dp[i-3] + dp[i-2] + dp[i-1];
            dp.push(v);
        }

        dp[n as usize]
    }
}