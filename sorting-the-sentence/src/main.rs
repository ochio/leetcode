impl Solution {
    pub fn sort_sentence(s: String) -> String {
        let mut sentence:Vec<&str> = s.split(' ').collect();

        sentence.sort_by(|a,b| a.chars().last().unwrap().cmp(&b.chars().last().unwrap()));

        sentence.iter().map(|mut word| {
            let mut s = word.to_string();
            s.pop();
            s
        }).collect::<Vec<String>>().join(" ")

    }
}