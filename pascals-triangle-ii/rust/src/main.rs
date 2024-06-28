impl Solution {
    pub fn get_row(row_index: i32) -> Vec<i32> {
        let row_index = row_index as usize;
        let mut ans = vec![vec![1]];

        for i in 1..=row_index {
            let mut tmp = vec![1];
            for j in 1..i {
                let v = ans[i - 1][j -1] + ans[i -1][j]; 
                tmp.push(v);
            }
            tmp.push(1);
            ans.push(tmp);
        }

        ans[row_index].clone()

    }
}