use std::cmp;

impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut ans = -1;

        for j in (0..nums.len()).rev() {
            for i in (0..j).rev() {
                if nums[i] < nums[j] {
                    ans = cmp::max(nums[j] - nums[i], ans);
                }
            }
        }
        ans
    }
}
