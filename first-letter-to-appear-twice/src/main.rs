use std::collections::HashMap;

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut log: HashMap<char, i32> = HashMap::new();
        let mut ans = ' ';
        for c in s.chars() {
            *log.entry(c).or_insert(0) += 1;
            if log.get(&c).unwrap() == &2 {
                ans = c;
                break;
            }
        }
        ans
    }
}