impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut ans = vec![];

        if num_rows >= 1 {
            ans.push(vec![1]);
        }

        for i in 1..num_rows {
            let mut tmp = vec![1];
            for j in 1..i {
                let v = ans[i as usize - 1][j as usize -1] + ans[i as usize -1][j as usize ]; 
                tmp.push(v);
            }
            tmp.push(1);
            ans.push(tmp);
        }

        ans
    }
}