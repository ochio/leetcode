impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        let mut ans = 0;
        for i in (1..=arr.len()).step_by(2) {
            let mut sum = 0;
            for j in 0..arr.len() {
                if j + i > arr.len() {
                    break;
                }
                sum += arr[j..j+i].iter().sum::<i32>();
            }
            ans += sum;
        }
        ans
    }
}