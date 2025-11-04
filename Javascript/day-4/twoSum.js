/*
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
*/

// Brute Force method :
/*
    The brute force method is a simple. 
    Loop through each elemnt x and find 
    if there is another value that equals 
    to target-x
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const result = {};
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (target - num in result) {
            return[i,result[target-num]];
        }
        result[num] = i;
    }
    
};

let nums1 = [2,7,8,11];
let target1 = 9;
console.log("Tast case 1:", twoSum(nums1,target1));

console.log("Test case 2:",twoSum([3,5,7,10],17));