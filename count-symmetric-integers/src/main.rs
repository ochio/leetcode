impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut ans = 0;
        for num in low..=high {
            let ary:Vec<char> = num.to_string().chars().collect();
            let length = ary.len();
            if length % 2 == 1 {
                continue;
            }

            let mut sum1 = 0;
            for i in 0..length/2 {
                sum1 += ary[i] as i32 - 48;
            }

            let mut sum2 = 0;
            for i in length/2..length {
                sum2 += ary[i] as i32 - 48;
            }

            if sum1 == sum2 {
                ans += 1;
            }

        }
        ans
    }
}