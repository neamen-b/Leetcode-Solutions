/**
 * @param {number[]} nums
 * @return {number}
 */


function countElements(nums){
    n = nums.length
    // Sort in non-decreasing
    nums.sort((a,b)=>a-b);
    var count = 0;
    var min = nums[0];
    var max = nums[n - 1]

    for (var i = 0; i < n; i++){
        console.log(`${min} ${max} ${nums[i]}`)
        if (min < nums[i] && nums[i] < max){
            count++;
        }
    }
    return count;
}


function CountElements2(nums){
    var min = Infinity;
    var max = -Infinity;

    for(var i = 0; i < nums.length; i++){
        min = Math.min(min, nums[i]);
        max = Math.max(max, nums[i]);
    }

    if(min === max){
        return 0;
    }
    freq_table = new Map();

    for (var i = 0; i < nums.length; i++){
        if(freq_table.has(nums[i])){
            freq_table.set(nums[i], freq_table.get(nums[i]) + 1);
        }
        else{
            freq_table.set(nums[i], 1);
        }
    }
    console.log(freq_table, min, max)
    console.log(freq_table[min], freq_table[max])
    return nums.length - freq_table.get(min) - freq_table.get(max)
}
console.log(CountElements2([11,7,11,15]));