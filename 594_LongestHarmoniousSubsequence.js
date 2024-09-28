/**
 * Initial thoughts:
 *  Quite lost honestly
 * 
 */


/**
 * @param {number[]} nums
 * @return {number}
 */


let findLHS = function(nums){
    // Map to serve as frequency distribution table
    let myMap = new Map();

    for (let num of nums){
        // console.log(myMap);
        // Increment frequency if inside
        if(myMap.has(num)){
            myMap.set(num, myMap.get(num)  + 1 );
        }
        // Add with frequency =1
        else{
            myMap.set(num, 1);
        }
    }

    // Object.keys() does not work for maps. Only for regular JS objects
    // for(key of Object.keys(myMap)){
    //     console.log(key);
    // }
    // Store sum of frequencies for key and key + 1 if exists
    let freq_sum = 0;
    
    // For each key in map
    for (key of myMap.keys()){
        // console.log(key);
        // If there exisits an entry with key that is key + 1
        if (myMap.has( key + 1)){
            // If sum > freq, then freq = sum , else stay the same
            freq_sum = (myMap.get(key) + myMap.get(key + 1)) > freq_sum ? (myMap.get(key) + myMap.get(key + 1)) : freq_sum;
        }
    }

    return freq_sum;
}


console.log(findLHS([1,1,1,1]));