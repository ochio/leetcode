impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut emp = 0;
        let mut ans = 0;
        let mut bottles = num_bottles;

        while true {
            ans += bottles;
            let new_bottles = (bottles + emp) / num_exchange;
            emp = (bottles + emp) % num_exchange;
            bottles = new_bottles;
            

            if new_bottles == 0 {
                break;
            }
        }

        ans
    }
}