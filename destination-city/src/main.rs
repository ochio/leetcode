use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn dest_city(paths: Vec<Vec<String>>) -> String {
        let mut p: HashMap<String, Vec<String>> = HashMap::new();
        let mut s: HashSet<String> = HashSet::new();

        for path in paths {
            let from = &path[0];
            let to = &path[1];
            p.entry(from.to_string()).or_insert(vec![]).push(to.to_string());
            s.insert(from.to_string());
            s.insert(to.to_string());
        }

        let mut ans = "";
        for city in s.iter() {
            match p.get_mut(city) {
                Some(_) => (),
                None => ans = city
            }
        };
        ans.to_string()
    }
}