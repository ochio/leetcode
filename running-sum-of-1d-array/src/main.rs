impl Solution {
    pub fn running_sum(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![nums[0]];
        for i in 1..nums.len() {
            let sum = ans[i-1] + nums[i];
            ans.push(sum);
        }
        ans
    }
}