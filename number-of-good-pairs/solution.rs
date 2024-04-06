impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut count = 0;
        for (i, val1) in nums.iter().enumerate() {
            for (j, val2) in nums.iter().enumerate() {
                if val1 == val2 && i < j {
                    count += 1;
                }
            }
        }
        count
    }
}
