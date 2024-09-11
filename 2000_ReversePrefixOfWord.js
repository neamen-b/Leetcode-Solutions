/**
 * Initial thougts:
 *  Use a stack to add the charcters until you see ch, then concaternate in reverse and "n concatenate" to word
 * 
 *  for each character in word, add it to a stack 
 *      if char is d, then add it to stack and make string from chars in stack
 *                     then add to string
 *      else
 *          add char to s
 
 */


/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */

let reversePrefix = function(word, ch) {

    // stack for storing prefix characters
    character_stack = [];
    prefix_array = [];

    // If empty, return word
    if (word.length === 0){
        return word;
    }

    // For each char in word
    // Very interesting lesson here. let index in word creates an indez that is a string but can be used to index word
    // However, you cannot use it as a pure indexing number and do something like word[index + 1]
    // So either use the good old for loop or typecast when needed as a number
    for (let index in word) {
        // If the char is ch, add to stack and pop stack till empty to form reversed prefix
        if (word[index] === ch){
            character_stack.push(word[index]);

            // console.log(character_stack);

            // This scales better because arrays are mutable and we are not creating a new string each time
            // Better for larger datasets
            while(character_stack.length > 0){
                prefix_array.push(character_stack.pop());
                // console.log(prefix_array);    
            }

            // while (!character_stack){
            //     // console.log(character_stack.pop());
            //     // This shoudl create a new string each time since strings are immutable. Kind of inefficient
            //     prefix = prefix + character_stack.pop();
            // }
            // console.log(prefix);

            // concatenate the remaining substring from word and prefix
            // Index + 1 because it is inclusive
            // console.log(word.substring(index + 1));
            // Type casting index to number because it is a string
            return prefix_array.join('') + word.substring(Number(index) + 1);
        }
        else {
            // Push to stack
            character_stack.push(word[index]);
        }
    }
    // If ch not found, return word
    return word;

}


console.log(reversePrefix('abcdefd', 'd'));