/**
 * Initial thoughts
 * 
 * 1. If the string is empty, then return empty string
 *      Can check this by looking at the length of the string
 * 
 * 2. iF the length of the string is 1:
 *      Two possibilities
 *          a. It is a letter
 *          b. It is a number
 * 
 *          if number remove and return empty
 *          else: leave as is
 * 3. Iteration
 *      Basic idea is to find the digit each time, remove it and if exiss remove letter to the left
 *      example
 *              hello2bru3
 *      First pass
 *          find 2, remove 2 and o  -> s = hellbro3
 *      second pass
 *          find 3, remove 3 and u  -> s = hellbr
 * 
 *      Now I can keep track of where I stopped last time by using a pointer to make it more efficient
 *      First pass   lastvalid = 'l' in hello2bru3, so start next iteration from l
 * 
 * 4. Implementation
 *      LIFO "stack" to keep track of characters
 *      iterate over s
 *          if character, push to stack
 *          elif number, pop stack /This removes the character before this currency number
 * 
 *      ISSUE: What if the first index is a number?
 *              Just return the stack as string because it will be empty
 * 
 * 5. Execution?
 * 
 */



/**
 * @param {string} s
 * @return {string}
 */
let ClearDigits = function(s){

    // Create empty stack
    let character_stack = [];


    for (let character of s){
        
        // If character cannot be turned into a number, add to the stack
        // Number() returns NaN if character is no a number, isNaN checks for NaN
        if ( isNaN(Number(character)) ) {
            character_stack.push(character);
        } 
        // If number, don't add it and pop stack, i.e., remove last non-digit element to the left
        else {

            // Return undefined if array is empty
            character_stack.pop();
        }

    }
    // Return stack as string
    return character_stack.join('');

    // Testing
    // console.log(character_stack);
    // This enumerates the string s which is weird
    // The difference turned out to be the keyword 'in'
    // 'of' lets you iteratre over it
    // for (let character in s) {
    //     console.log(character);
    // };

}

let ans = ClearDigits("");
console.log(ans);