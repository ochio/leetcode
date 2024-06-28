// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }

// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        
        fn rec(node: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32{
            let mut sum = 0;
            if let Some(n) = node {
                let n = n.borrow();
                if low <= n.val && n.val <= high {
                    sum += n.val;
                }

                if n.left.is_some() {
                    sum += rec(&n.left, low, high);
                }

                if n.right.is_some() {
                    sum += rec(&n.right, low, high);
                }

            }
            sum
            

        }

        rec(&root, low, high)

    }
}