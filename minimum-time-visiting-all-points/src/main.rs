impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut ans = 0;

        fn d(from: &Vec<i32>, to: &Vec<i32>) -> i32 {
            let a0 = (to[0] - from[0]).abs();
            let a1 = (to[1] - from[1]).abs();
            a0.min(a1) + (a1 - a0).abs()
        }

        for i in 1..points.len() {
            ans += d(&points[i-1], &points[i]);
        }

        ans
    }
}