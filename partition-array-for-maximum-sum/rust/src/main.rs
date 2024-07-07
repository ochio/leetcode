impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let mut dp = vec![0; n + 1];
        let k = k as usize;

        for i in 1..=n {
            let mut m = 0;
            for j in 1..=k.min(i) as usize {
                m = m.max(arr[i-j]);
                dp[i] = dp[i].max(dp[i-j] + m * j as i32)
            }
        }

        dp[n]
    }
}