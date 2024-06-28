impl Solution {
    pub fn shuffle(nums: Vec<i32>, n: i32) -> Vec<i32> {
        let mut ans = Vec::new();

        for i in 0..n{
            ans.push(nums[i as usize]);
            ans.push(nums[i as usize + n as usize]);
        }

        ans
    }
}