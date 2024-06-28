impl Solution {
    pub fn max_value(n: String, x: i32) -> String {
        let mut num = n.as_bytes().to_vec();
        let c = char::from_digit(x as u32, 10).unwrap();
        let x = c as u8;

        if num[0] == b'-' {
            for i in 1..num.len() {
                if num[i] > x {
                    num.insert(i, x);
                    return String::from_utf8(num).unwrap();
                }
            }
            num.push(x);
            return String::from_utf8(num).unwrap();
        } else {
            for i in 0..num.len() {
                if num[i] < x {
                    num.insert(i, x);
                    return String::from_utf8(num).unwrap();
                }
            }
            num.push(x);
            return String::from_utf8(num).unwrap();
        }
    }
}