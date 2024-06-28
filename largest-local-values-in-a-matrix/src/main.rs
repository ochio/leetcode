impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n = grid.len() - 2;
        let mut ans = vec![vec![0;n];n];

        for i in 0..n {
            for j in 0..n {
                let mut local = 0;
                for r in i..=i+2 {
                    for c in j..=j+2{
                        local = local.max(grid[r][c]);
                    }
                }
                ans[i][j] = local;
            }
        }

        ans
    }
}