impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut ans = vec![0];

        for i in 1..=n {
            let index = i / 2;
            let v = if i % 2 == 0 { ans[index as usize] } else { ans[index as usize] + 1 };
            ans.push(v)
        }

        ans
    }
}