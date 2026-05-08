impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let (mut ls, mut rs) = (0i32, nums.len() as i32 -1);
        while ls <= rs {
            let mid = ls + (rs-ls)/2;
            if nums[mid as usize] > target {
                rs = mid -1;
            } else if nums[mid as usize] < target {
                ls = mid +1;
            } else {
                return mid;
            }
        }
        -1
    }
}
