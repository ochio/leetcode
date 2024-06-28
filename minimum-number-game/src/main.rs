impl Solution {
    pub fn number_game(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = nums.clone();
        ans.sort();
        for i in (0..ans.len()).step_by(2) {
            (ans[i], ans[i+1]) = (ans[i+1], ans[i])
        }
        ans
    }
}