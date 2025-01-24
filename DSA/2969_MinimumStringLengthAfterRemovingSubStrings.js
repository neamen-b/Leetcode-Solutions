/**
 * Initial thoughs:
 * 1. Use a stack
 *      Iteratte over s and under certain conditions, either add or pop from the stack
 * 
 * 2. If s is empty, return 0
 * 
 * 3. For each character in s
 *      If B look at stack[end]
 *          If stack[end] is A, stack.pop()
 *      If D, look at stack[end]
 *          If stack[end] is C, stack.pop()
 *      else
 *          stack.push(character)
 */
/**
 * @param {string} s
 * @return {interger}
 */


let minLength = function(s){

    // stack to store valid characters
    character_stack = [];

    // Neat wat of accessing the last element in an array
    // console.log(character_stack.at(-1))

    // If string is empty
    if (s.length === 0){
        return 0;
    };

    // For each character in s
    for (let character of s){

        // If char is 'D' and character before it is 'C', remove 'C' and don't add 'D'
        if (character === 'D' && character_stack.at(-1) === 'C'){
            character_stack.pop();
        }
        // If char is 'B' and character before is 'A', remove 'A' and don't add 'B'
        else if (character === 'B' && character_stack.at(-1) === 'A'){
            character_stack.pop();
        }
        else {
            character_stack.push(character);
        }
    }

    return character_stack.length;
}

console.log(minLength(''));