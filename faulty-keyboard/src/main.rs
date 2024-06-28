impl Solution {
    pub fn final_string(s: String) -> String {
        let mut ary: Vec<char> = vec![];

        for c in s.chars() {
            if c == 'i' {
                ary.reverse();
            } else {
                ary.push(c)
            }
        }
        ary.into_iter().collect()
    }
}