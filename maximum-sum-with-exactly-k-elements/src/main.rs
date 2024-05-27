impl Solution {
    pub fn maximize_sum(nums: Vec<i32>, k: i32) -> i32 {
        let m = nums.iter().max().unwrap();
        let mut sum = 0;

        for i in 0..k {
            sum += i + m;
        }

        sum
    }
}