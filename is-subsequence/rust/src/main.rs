impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let mut i = 0;
        let n = s.len();

        for char in t.chars() {
            if i < n && s.chars().nth(i).unwrap() == char {
                i += 1;
            }
        }

        i == s.len()
    }
}