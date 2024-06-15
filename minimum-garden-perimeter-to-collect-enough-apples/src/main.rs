impl Solution {
    pub fn minimum_perimeter(needed_apples: i64) -> i64 {
        let mut apples: Vec<i64> = vec![0];
        let a:i64 = 12;
        let mut i = 1;

        while apples.last().unwrap() <= &(10 as i64).pow(15) {
            apples.push(a * i * i + apples.last().unwrap());
            i += 1;
        }

        let mut ng =  -1 as isize;
        let mut ok = apples.len() as isize;
        while ok - ng > 1 {
            let mid = (ok + ng) / 2;
            if needed_apples <= apples[mid  as usize] {
                ok = mid;
            }else{
                ng = mid;
            }
        }

        (ok as i64) * 2 * 4
    }
}