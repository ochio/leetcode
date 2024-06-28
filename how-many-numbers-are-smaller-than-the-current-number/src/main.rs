impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = vec![];

        for i in 0..nums.len() {
            let mut cnt = 0;
            for j in 0..nums.len() {
                if i == j {
                    continue
                } else {
                    if nums[j] < nums[i] {
                        cnt += 1;
                    }
                }
            }
            ans.push(cnt);
        }

        ans
    }
}