impl Solution {
    pub fn is_same_after_reversals(num: i32) -> bool {
        num == 0 || num.to_string().chars().last().unwrap() != '0'
    }
}