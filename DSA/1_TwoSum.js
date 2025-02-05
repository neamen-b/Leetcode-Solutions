/**
 * Intitial thoughts:
 * 
 *      Two pointer approach
 *      1. Sort array nums somehow
 *      2. See if opposite end sum up to target
 *              yes?
 *                  return indices
 *              < ?
 *                  increase start
 *              > ?
 *                  decrease end
 *         
 *          Sorting = O(nlogn)
 *          opposites traversal = O(n)
 * 
 *          program = O(nlogn)
 *          
 *          PROBLEM:
 *          Once the array is sorted, the original indices are not maintained
 *              Cannot a use a hashmap because there might be duplicate elements
 *          create objects
 *              value : index
 * 
 *         Set Approach
 *         1. Add values to set
 *         2. For each value, find if (val - tgt) exists in complement
 * 
 *          Adding to and traversing set  = O(n)
 *          
 *          Tricky part is the complement part? How do I get the complement of the element?
 * 
 *              Here's how : Remove the element before you check the compliment then add it back
 *                  Adding and removing is order one so we are good.
 * 
 *      
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * Set approach
 *
 */


let twoSum = function(nums, target){

    // Map initialized with nums. index -> nums becuase keys have to be unique
    let myMap = new Map();

    for (let index = 0; index < nums.length; index++){
        myMap.set(index, nums[index]);
    }
    // console.log(mySet);

    for (let num of myMap.keys()){

        // Keeping track of num to add back in case it is removed from memory
        let temp = myMap.get(num);
        // Remove from set
        myMap.delete(num);

        if(myMap.has(target - temp)){
            return true;
        }
        // Add back
        myMap.add(temp);
    }

    return
}


// twoSum([12,3], 4);

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * Two pointer approach with sort
 */

let twoSum2 = function(nums, target){

    let num_and_index = [];

    for (let index = 0; index < nums.length; index++){
        // Add as tuple (value, index)
        num_and_index.push([nums[index], index]);
    }
    // sorts in non-descending order
    // given two tuples, sort on first element
    num_and_index.sort((a,b)=> a[0]-b[0]);

    // console.log(num_and_index);
    
    let start = 0;
    let end  = num_and_index.length - 1;
    
    // console.log(num_and_index[start][0], num_and_index[end][0]);
    while (start < end){

        if(num_and_index[start][0] + num_and_index[end][0] < target){
            start++;
        }
        else if(num_and_index[start][0] + num_and_index[end][0] > target){
            end--;
        }
        else{
            return [num_and_index[start][1],num_and_index[end][1]];
        }
    }
}
console.log(twoSum2([3,2,4], 6));