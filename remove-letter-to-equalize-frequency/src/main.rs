use std::collections::HashMap;

impl Solution {
    pub fn equal_frequency(word: String) -> bool {
        let mut hash = HashMap::new();

        for c in word.chars() {
            hash.entry(c).and_modify(|n| *n+=1).or_insert(1);
        }

        if hash.keys().len() == 1 {
            return  true;
        }

        let mut hash2 = HashMap::new();

        for key in hash.keys(){
            let n = hash.get(key).unwrap();
            let count = n.to_string();
            hash2.entry(count).and_modify(|n| *n+=1).or_insert(1);
        }


        if let Some(key) = hash2.keys().next() {
            if hash2.keys().len() == 1 && key == "1" {
                return true;
            }
        }

        if hash2.keys().len() == 2 {
            let mut keys:Vec<i32> = hash2.keys().map(|c| c.parse().unwrap()).collect();
            keys.sort();

            let small = keys[0].to_string();
            let large = keys[1].to_string();
            if *hash2.get(&large).unwrap() == 1 && keys[0] == keys[1] - 1{
                return  true;
            }

            if small == "1" && *hash2.get(&small).unwrap() == 1{
                return  true;
            }
        }
        false

    }
}