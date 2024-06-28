impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let mut ans = 0;
        let n = strs.len();
        let m = strs[1].len();

        for i in 0..m {
            let mut c = 'a';
            for j in 0..n {
                let tmp = strs[j].chars().nth(i).unwrap();
                if c <= tmp {
                    c = tmp;
                }else{
                    ans += 1;
                    break;
                }
                
            }
        }
        ans
    }
}