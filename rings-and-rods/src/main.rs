use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn count_points(rings: String) -> i32 {
        let mut lods: HashMap<char, HashSet<char>> = HashMap::new();

        for i in (0..rings.len()).step_by(2) {
            let color = rings.chars().nth(i).unwrap();
            let lod = rings.chars().nth(i + 1).unwrap();
            lods.entry(lod).or_insert(HashSet::new()).insert(color);
        }

        let mut ans = 0;

        for colors in lods.values() {
            if colors.len() == 3 {
                ans += 1
            }
        }
        ans
    }
}