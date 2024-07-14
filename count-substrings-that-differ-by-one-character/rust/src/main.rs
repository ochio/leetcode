impl Solution {
    pub fn count_substrings(s: String, t: String) -> i32 {
        let n = t.len();
        let s = s.as_bytes();
        let t = t.as_bytes();

        fn count_diff(s_sub: &[u8], t_sub:&[u8]) -> bool {
            let mut count = 0;
            for i in 0..s_sub.len(){
                if s_sub[i] != t_sub[i] {
                    count += 1;
                }
            }
            count == 1
        }

        fn diff(s_sub: &[u8], t:&[u8]) -> i32{
            let l = s_sub.len();
            let n = t.len();
            let mut count = 0;
            for i in 0..t.len() {
                if i + l > n {
                    break;
                }

                let t_sub = &t[i..i+l];

                if count_diff(s_sub, t_sub) {
                    count += 1;
                }
            }
            count
        }

        let mut ans = 0;
        for i in 0..s.len() {
            for j in i+1..=s.len() {
                let s_sub = &s[i..j];
                ans += diff(s_sub, t);
            }
        }
        ans
    }
}