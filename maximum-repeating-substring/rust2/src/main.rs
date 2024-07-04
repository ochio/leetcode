impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let n = sequence.len();
        let m = word.len();
        let mut dp = vec![0; n + 1]; m + 1;
        let mut ans = 0;

        for i in m..=n {
            if &sequence[i-m..i] == word {
                dp[i] = dp[i-m] + 1;
                ans = ans.max(dp[i])
            }
        }
        ans
    }
}