/**
 * Initial thoughts
 *  Screams sliding window problem
 *      1. keep a window of size k in a map (index -> value)
 *          chose to use index becasue key values have to be unique
 *      
 *      for num in nums:
 *          if (map.size < k){
 *             
 *              }
 */


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 * 
 * Implemented using a Map which turned out to be very slow for some reason even though it is O(n)
 */

let findMaxAverage = function(nums,k){
    // Window of max length k
    let myMap  = new Map();
    // sum of values in winoow 
    let average, sum = 0;
    // Largest average
    let max_average = -Infinity;

    for (let index = 0; index < nums.length; index++){
        // console.log("map size",myMap.size);
        // console.log(sum);
        // console.log(nums[index]);
        
        // add to map while size is less than window size
        // if (myMap.size < k){
        myMap.set(index, nums[index]);
        // Update sum for each window
        sum = sum + nums[index];
        // console.log(`sum before delete ${sum}`)
        
        
        if(myMap.size >= k) {
            average = sum / k;
            // console.log(`average ${average}`);
            // See if this average is is the greatest
            max_average = average > max_average ? average : max_average;
            
            // Remove the oldest entry from the sum because window is moving 
            sum = sum - myMap.get(index - k + 1);

            // console.log(`sum after delete ${sum}`)
            // Remove the oldest entry from the map
            myMap.delete(index - k + 1 );
            // console.log(typeof(index - k + 1)
        }
    }

    // keys are stored as strings not numbers
    // for(let key of myMap.keys()){
    //     console.log(typeof(key));
    // }

    return max_average;
}


// console.log(findMaxAverage([5], 1));

/**
 * @param {number[]} nums
 * @param {numver} k
 * @return {number}
 * Sliding window with just two pointers
 * Still slow for some annoying reason. Perhaps the infinity?
 * EUREKA! It was becuase I was creating a new variable of ave each time. Spelling can cost you time!
 */

let findMaxAverage2 = function(nums, k){

    // Window view into nums of size k 
    let start = 0;
    // k - 1 since 0 indexed
    let end = start + k - 1;
    //average
    let ave, sum = 0;
    // max average
    let max_av = -Infinity;

    for (let index = 0; index < nums.length; index++){

        sum = sum + nums[index];

        if(index >= end){
            ave = sum / k;
            max_av = ave > max_av ? ave : max_av;
            sum = sum - nums[start];
            start++;
            end++;
        }
    }
    return max_av;
}

console.log(findMaxAverage2([1,12,-5,-6,50,3], 4));