impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut sum = 0;
        for i in 0..chars.len() - 1 {
            let diff = (chars[i] as i32 - chars[i + 1] as i32).abs();
            sum += diff
        }
        sum
    }
}
