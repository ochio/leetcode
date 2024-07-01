impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min = prices[0].clone();
        let mut ans = 0;

        for p in prices {
            ans = ans.max(p - min);
            min = min.min(p);
        }

        ans
    }
}