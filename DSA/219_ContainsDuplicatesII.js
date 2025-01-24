/**
 * Intital thoughts:
 *  Using a map to track values and indices
 *  Didn't really know hot to do a sliding window
 * 
 * 
 * Sliding windows
 *      
 *      windows  = Map (value -> index)  size limited to k
 *      
 *      for num in nums:
 *          if windows.size > k:
 *              windows.remove(0)
 *          
 *          if windows.has(num):
 *              
 *              if windows[num] - indexof(num) <= k:
 *                  return true
 *          else:
 *              windows.push(num, indexof(num))
 *      return false
 */



/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */


let containsNearbyDuplicate = function(nums, k){
    let myMap = new Map();
    // THe index of the last number added to my window
    let index_of_last_entry = -1;

    // for each number
     for (let index in nums){
        // Casting to type number becuase for loop gives out a string
        index = Number(index);

        // Keeping window k size
        if(myMap.size > k){
            // console.log(`Window before adj -> ${[...myMap.values()]}`);
            // remove the element that was added k indices ago
            myMap.delete(nums[index_of_last_entry-k]);
        }
        // Checks if the num exists as a key
        if (myMap.has(nums[index])){

            // Check indexof(num) with indexof(key)
            // Absolute value becuase need just distance
            if (Math.abs(index - myMap.get(nums[index])) <= k){
                return true;
            }
        }
        // Add it if not
        else{
            // Set number -> index in nums
            myMap.set(nums[index],index);
            // set index of last element
            index_of_last_entry = index;
            
            // console.log(`Window after adj -> ${[...myMap.keys()]}`);
        }
     }

     return false;
}

console.log(containsNearbyDuplicate([1,2,3,1,2,3], 2));