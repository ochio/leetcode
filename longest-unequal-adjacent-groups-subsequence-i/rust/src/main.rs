impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut ans = vec![words[0].clone()];
        let mut b = groups[0];

        for i in 1..words.len() {
            if groups[i] != b {
                b = groups[i];
                ans.push(words[i].clone());
            }
        }

        ans
    }
}