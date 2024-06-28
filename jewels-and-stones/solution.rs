use std::collections::HashMap;

impl Solution {
    pub fn num_jewels_in_stones(jewels: String, stones: String) -> i32 {
        let mut map = HashMap::<char, i32>::new();
        for s in stones.chars() {
            *map.entry(s).or_insert(0) += 1;
        }

        let mut count = 0;

        for j in jewels.chars() {
            if map.get(&j).is_some() {
                count += map[&j];
            }
        }

        count
    }
}
