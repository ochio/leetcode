impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        let v : Vec<&str>= s.split(' ').collect();
        v[..k as usize].join(" ")
    }
}