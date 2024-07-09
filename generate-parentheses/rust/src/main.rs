impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut ans = vec![];

        fn dfs(open: i32, close: i32, s: String, n: i32, ans: &mut Vec<String>) {
            if s.len() == (n * 2) as usize {
                ans.push(s.to_string());
                return;
            }

            if open < n {
                dfs(open + 1, close, s.to_string() + "(", n, ans)
            }

            if open > close {
                dfs(open, close + 1,  s.to_string() + ")", n, ans)
            }
        }

        dfs(0, 0, String::from(""), n, &mut ans);

        ans
    }
}