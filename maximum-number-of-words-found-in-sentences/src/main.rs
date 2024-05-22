impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut ans = 0;

        for sentence in sentences {
            let mut cnt = 0;
            for c in sentence.chars() {
                if c == ' ' {
                    cnt += 1;
                }
            }
            cnt += 1;
            ans = ans.max(cnt);
        }

        ans
    }
}