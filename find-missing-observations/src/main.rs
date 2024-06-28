impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let remain = mean * (rolls.len() as i32 + n) - rolls.iter().sum::<i32>(); 
        let mut ans: Vec<i32> = vec![];

        let base = remain / n;
        let r_num = remain % n;

        let mut ans = vec![];

        

        if base < 1 || base > 6 {
            return [].to_vec();
        }

        for _ in 0..n {
            ans.push(base)
        }

        for i in 0..r_num {
            ans[i as usize] += 1;
            if ans[i as usize] == 7 {
                return [].to_vec();
            }
        }
        return ans;
    }
}