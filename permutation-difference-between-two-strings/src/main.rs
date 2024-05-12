impl Solution {
    pub fn find_permutation_difference(s: String, t: String) -> i32 {
        let mut sum = 0;
        for (i,char) in s.chars().enumerate() {
            let j = t.find(char).unwrap();
            let num = (i as i32)-(j as i32);
            sum += num.abs();
        }
        sum
    }
}