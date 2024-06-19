impl Solution {
    pub fn max_power(s: String) -> i32 {
        let mut ans = 1;
        let mut cnt = 1;
        for i in 1..s.len() {
            if s[i..i+1] == s[i-1..i] {
                cnt += 1
            } else {
                ans = ans.max(cnt);
                cnt = 1;
            }
        }
        ans = ans.max(cnt);
        ans
    }
}