impl Solution {
    pub fn count_substrings(s: String) -> i32 {
        let mut ans = 0;
        let s = s.as_bytes();
        let n = s.len() as isize;
        fn count(mut left: isize, mut right: isize, n: isize, s: &[u8]) -> i32{
            let mut cnt = 0;

            while 0 <= left && right < n {
                if s[left as usize] == s[right as usize] {
                    cnt += 1;
                    left -= 1;
                    right += 1;
                } else {
                    break;
                }
            }
            cnt
        }



        for i in 0..n as isize {
            ans += count(i, i, n, &s);
            ans += count(i, i+1, n, &s);
        }
        ans
    }
}