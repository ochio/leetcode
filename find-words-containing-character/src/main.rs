impl Solution {
    pub fn find_words_containing(words: Vec<String>, x: char) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        for i in 0..words.len() {
            let word = &words[i];
            if word.contains(x){
                ans.push(i as i32)
            }
        }
        ans
    }
}