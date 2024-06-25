impl Solution {
    pub fn fib(n: i32) -> i32 {
        let mut f = vec![0,1];

        for i in 2..=n {
            let v = f[i as usize -1] + f[i as usize -2];
            f.push(v);
        }

        f[n as usize]
    }
}