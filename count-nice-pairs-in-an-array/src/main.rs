use std::collections::HashMap;

impl Solution {
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        fn rev(num: i32) -> i32 {
            num.to_string().chars().rev().collect::<String>().parse::<i32>().unwrap()
        }

        let mut ans = 0;
        let mut map = HashMap::new();

        for i in 0..nums.len() {
            let key = nums[i] - rev(nums[i]);

            let mut v = map.entry(key).or_insert(0);
            ans += *v;
            ans %= 1000000000 + 7;
            *v += 1;
        }

        ans
    }
}