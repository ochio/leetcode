impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        for n in &nums {
            ans.push(*n);
        }
        for n in &nums {
            ans.push(*n);
        }
        ans
    }
}
