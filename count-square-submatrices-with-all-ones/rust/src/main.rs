use std::cmp::min;

impl Solution {
    pub fn count_squares(matrix: Vec<Vec<i32>>) -> i32 {
        let m = matrix.len();
        let n  = matrix[0].len();
        let mut dp = vec![vec![vec![0; min(m, n)]; n]; m];
        let mut ans = 0;


        for i in 0..m {
            for j in 0..n {
                for k in 0..min(m, n) {
                    if k == 0 && matrix[i][j] == 1 {
                        dp[i][j][k] = 1;
                        ans += 1
                    }

                    if i >= 1 && j >= 1  && k >= 1 {
                        if matrix[i][j] == 1 && dp[i][j-1][k-1] == 1 && dp[i-1][j][k-1] == 1 && dp[i -1][j-1][k-1] == 1 {
                            dp[i][j][k] = 1;
                            ans += 1;
                        }
                    }
                }
            }
        }

        ans
    }
}