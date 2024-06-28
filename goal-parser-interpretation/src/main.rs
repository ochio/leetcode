impl Solution {
    pub fn interpret(command: String) -> String {
        let mut ans:String = "".to_string();
        let mut tmp = "";
        for (i,c) in command.chars().enumerate() {
            match c {
                'G' =>{ ans += "G"},
                'a' => continue,
                'l' => continue,
                ')' => continue,
                _ => {
                    if command.chars().nth(i+1).unwrap() == ')' {
                        ans += "o";
                    }else{
                        ans += "al";
                    }
                }
            }
        }
        ans.to_string()
    }
}