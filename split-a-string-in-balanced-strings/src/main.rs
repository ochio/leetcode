impl Solution {
    pub fn balanced_string_split(s: String) -> i32 {
        let mut r_num = 0;
        let mut l_num = 0;
        let mut ans = 0;

        for (_, c) in s.chars().enumerate() {
            if c == 'R' {
                r_num += 1;
            } else {
                l_num += 1
            }

            if r_num == l_num {
                ans += 1;
                r_num = 0;
                l_num = 0;
            }
            
        }
        ans
    }
}