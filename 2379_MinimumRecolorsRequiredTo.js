/**
 * Initial thoughts
 *      Sliding windows of size k
 * 
 *      while (end < len(blocks))
 *          count_whites in blocks[start ... end]
 *          if count < min then  min = count
 *          start++
 *          end++
 *          
 *          Big problem: How do I count? I am looking at N^2 if go through each subarray.
 *      
 */


/**
 * @param {number[]} blocks
 * @param {number} k
 * @return {number}
 * 
 * Using Sliding windows but n^2
 */

let minimumRecolors = function(blocks, k){

    // windows dtart and end
    let start = 0;
    let end = 0 + k - 1;
    let min = Number.POSITIVE_INFINITY;
    let count_1 = 0;

    let count_whites = function(start,end){
        let count = 0;
        for (let index = start; index <= end; index++){
            if(blocks[index] === "W"){
                count++;
            }
        }
        return count;
    }

    while( end < blocks.length){
        count_1 = count_whites(start, end);

        if (count_1 < min){
            min = count_1;
        }
        console.log(`start ${start}, end ${end}`);
        start++;
        end++;
    }

    return min;
}

let blocks = "WBBWWBBWBW";
// console.log(minimumRecolors(blocks, 2));


/**
 * 
 * @param {number} blocks 
 * @param {number} k 
 * @returns {number}
 * 
 * sliding windows but O(n)
 */
function min(blocks, k){
    let min = Number.POSITIVE_INFINITY;
    let start = 0;
    let end = start + k - 1;
    let count = 0;

    for (let index = start ; index <= end; index++){
        if(blocks[index] === "W"){
            count++;
        }
    }

    while (end < blocks.length){

        if(count < min){
            min = count;
        }
        if (blocks[start] === 'W'){
            count--;
        }
        start++; end++;
        if( blocks[end] === 'W'){
            count++;
        }
    }

    return min;
}

console.log(min(blocks, 7));