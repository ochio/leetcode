impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat.len();
        let m = mat[0].len();
        let mut ans = 0;

        for i in 0..n {
            for j in 0..m {
                let cell = mat[i][j];

                if cell == 0 {
                    continue;
                }

                let mut f = true;
                for k in 0..n {
                    if k == i {
                        continue;
                    }
                    if mat[k][j] == 1 {
                        f = false;
                        break;
                    }
                }

                for k in 0..m {
                    if k == j {
                        continue;
                    }
                    if mat[i][k] == 1 {
                        f = false;
                        break;
                    }
                }

                println!("{} {} {}", i , j , f);

                if f {
                    ans += 1
                }


            }
        }

        ans
    }
}