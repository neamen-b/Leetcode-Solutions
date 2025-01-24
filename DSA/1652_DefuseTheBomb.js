/**
 * Initial thoughts
 *      1. Sliding window since I searched for a problem by a technique
 *      n = code.length
 *      for num in code:
 *          if k>0:
 *              Copy_code[index] = sum (code[index + 1 ..... index + k])
 *          if k<0:
 *              Copy_code[index] = sum (code[index - 1...... index - k])
 *              
 *          Issue with k < 0 and k > 0:
 *              Code is cyclic but how do i tell the program that?
 *              It is not a linked list. Will get out of bounds 
 *              
 *          if k == 0:
 *              code[index] = 0
 * 
 * 2. post thoughts
 *      VERY SLOW. The nested loops causing the issue for large k. 
 *      O(n*k)
 *      O(n*n) if |k| == n
 *      Need to 
 *      
 * 
 */

/**
 * @param {number[]} code
 * @param {number} key
 * @return {number[]}
 */

let decrypt = function(code, k){
    // Array for decrypted numbers  
    let decrypted_code = [];
    let n = code.length;

    for (let index = 0; index < code.length; index++){
        
        if (k > 0){
            // holds sum of the next k elements
            let sum = 0;
            // from index + 1 to index + k
            for(let i = 1; i <= k; i++ ){
                // used cyclical indexing with modulo
                console.log(`index -> ${index}, next -> ${(index + i)%n}, next -> ${index + i}`);
                sum += code[(index + i) % n];
            }
            decrypted_code[index] = sum;
        }
        
        else if (k < 0){
            // sum
            let sum = 0;
            // from index - 1 to index - k
            for (let i = 1; i <= Math.abs(k); i++){
                console.log(`index -> ${index}, next_mod_index -> ${((index - i) + n) % n}, next_index -> ${index - i}`);
                sum += code[((index - i)+ n) % n];

                // i === 3 ? process.ext(0)  : 'go';
            }
            decrypted_code[index] = sum;
        }
        // k ==0
        else{
            decrypted_code[index] = 0;
        }
    }   
    
    return decrypted_code;

}

console.log(decrypt([2,4,9,3], -2));


// Cyclic indexing practice
/**
 * @param {number[]} code
 * @param {number} key
 */

let cyclic = function(code, key){
    n = code.length;
    //  over
    // n goes into 7 1 times and 2 is left. so index 7 -> index 2
    console.log(`7 -> ${code[7%n]}`);

    // under
    // add n to remove negative 

    console.log(`-2 -> ${code[(-2 % n + n) % n]}`);
}

// cyclic([1,2,3,4,5]);



// Sliding windows approach

let decrypter = function(code, k){
    // Window indices
    n = code.length
    for (let index = 0; index < n ; i++){

        if (k > 0){
            let start = (index + 1);
            let end = (index + k);

            if(end >= n){
                end = end % n;
            }
        }
        

    }
}