impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        let index = word.find(ch);

        if let Some(i) = index {
            word[..=i].chars().rev().collect::<String>() + &word[i+1..]
        } else {
            word
        }
    }
}