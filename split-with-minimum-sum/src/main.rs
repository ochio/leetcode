impl Solution {
    pub fn split_num(num: i32) -> i32 {
        let mut v: Vec<char> = num.to_string().chars().collect();

        v.sort();

        let mut num1 = String::new();
        let mut num2 = String::new();

        for (i , n) in v.iter().enumerate() {
            if i % 2 == 0 {
                num1 += &n.to_string();
            }else{
                num2 += &n.to_string();
            }
        }
        
        num1.parse::<i32>().unwrap() + num2.parse::<i32>().unwrap()
    }
}