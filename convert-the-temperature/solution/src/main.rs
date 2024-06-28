impl Solution {
    pub fn convert_temperature(celsius: f64) -> Vec<f64> {
        let mut ans = Vec::new();
        ans.push(celsius + 273.15);
        ans.push(celsius * 1.80 + 32.00);
        ans
    }
}
