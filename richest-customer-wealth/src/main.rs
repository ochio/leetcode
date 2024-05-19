
impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;

        for account in accounts {
            let sum:i32 = account.iter().sum();
            ans = ans.max(sum)
        } 

        ans
    }
}