/**
 * intitial thoughts
 *      1. Frequency distribution table implemented with HashTable\
 *          
 *          for nums in nums:
 *               if frequency of num > 1:
 *                  return num, num + 1
 */

/**
 * @param {number} nums
 * @return {number[]}
 */


let findErrorNums = function(nums){
    // freq dist table 
    let myMap = new Map();
    let n = nums.length;
    let duplicate = undefined;

    // Created freq table by pushing/updating freq in table
    for (let index = 0; index < n ; index++){
        
        // console.log(myMap);
        if(myMap.has(nums[index])){
            myMap.set(nums[index], myMap.get(nums[index]) + 1);
            
            // If freq > 1, duplicate has been found
            if(myMap.get(nums[index]) > 1){
                duplicate = nums[index];
            }
        }

        else{
            myMap.set(nums[index], 1);
        }
    }

    // Check which number is missing in table from 1 -> n
    for (let num = 1; num<=nums.length ; num++){

        if(!myMap.has(num)){
            return [duplicate, num];
        }
    }
}

console.log(findErrorNums([3,2,2]));