/**
 * Initial thought:
 *  1. Don't know how or when to stop for that matter, apart from when the sum equals 1
 * 
 * 2. Use modulo to get remainders ain the 10th, 100th, 1000th, and nth place and then sum the saures
 * 
 *      For example:
 *          a. n = 256
 *              256 % 10 (10th place didgits) = 25 * 10 + 6 = 6
 *              25 % 10 (100th place digit) = 2 * 10 + 5 = 5
 *              2  % 10 (1000th place) = 0 * 10 + 2 = 2
 *      
 *      quotient = n
 *      while quotient is > 0:
 *          modulo the quotient
 *          quotient  = floor(quotient/10)
 */

// let n = 256;
// let quotient = n;
// let sum = 0;

// let sums_set = new Set();
// while(sum !== 1  && sums_set.has(sum)){
//     sum = 0;
//     while(quotient > 0){
//         sum = sum + Math.pow(quotient % 10, 2);
//         // console.log(quotient % 10);
//         quotient = Math.floor(quotient / 10);
//     }

//     console.log(`Sum ${sum}`);
//     // if (sums_set.has(sum)){
//     //     console.log(false);
//     //     break;
//     // }
    
//     sums_set.add(sum);
    
//     if (sum === 1){
//         console.log(true);
        
//     }
//     quotient = sum;
// }

/**
 * @param {number} 
 * @return {boolean}
 */


let isHappy = function(n){
    let quotient = n;
    let sum = 0;
    let sums_set = new Set();

    while(sum !== 1){
        sum = 0;

        // Using modulo, extracts each 10th place digits and finds sum of sqaures
        while(quotient > 0){
            // Extract 10th place digit
            sum = sum + Math.pow(quotient % 10, 2);
            // console.log(quotient % 10);
            // Finds quotient an integer to preserve the 100th place digit
            quotient = Math.floor(quotient / 10);
        }
        
        // Troubleshooting
        console.log(`Sum ${sum}`);
        // if (sums_set.has(sum)){
        //     console.log(false);
        //     break;
        // }
        
        // this is where loops are detected. If seen again, loop - > Not happy
        if (sums_set.has(sum)){
            return false;
        }
        // else add to our sums
        else{
            sums_set.add(sum);
        }
        // the loop will stop but will not return anything so this included just for the return
        // could just return true outside the loop 
        if(sum === 1){
            return true;
        }
        quotient = sum;

    }
}


console.log(isHappy(256));