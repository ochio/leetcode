impl Solution {
    pub fn max_repeating(sequence: String, word: String) -> i32 {
        let mut i = 0;
        let mut ans = 0;
        loop {
            let w = word.repeat(i);
            if sequence.contains(&w) {
                ans = i;
            }
            if w.len() > sequence.len() {
                break;
            }
            i += 1;
        }
        ans as i32
    }
}