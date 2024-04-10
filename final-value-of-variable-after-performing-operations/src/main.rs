impl Solution {
    pub fn final_value_after_operations(operations: Vec<String>) -> i32 {
        let mut sum = 0;
        for o in operations {
            if o.contains("-") {
                sum -= 1;
            } else {
                sum += 1;
            }
        }
        sum
    }
}
