/**
 * Initial thoughts:
 * 
 *  1. Sort and compare works but is O(nlogn)
 *  2. If symmertric difference of the sets is {}, then they are anagrams
 *      I don't know the complexity of this operation
 *      ahh Won't work
 * \        There could be repeated letters in the word so no
 *  3. 
 *  
 *
 */


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */


let isAnagram = function (s, t) {
    // hashmap to keep count of letter occurence
    let myMap = new Map();
    // count for each character
    let count = 1;

    // each character in string s
    for (let char of s){
        if (myMap.has(char)){
            // console.log(myMap.get(char));
            myMap.set(char, myMap.get(char) + 1);
        }
        else{

            myMap.set(key = char , value = count);
        }
    }


    for (let char of t){
        if (myMap.has(char)){
            myMap.set(char, myMap.get(char) - 1);
        }
        // If does not have it, then difference.
        else {
            return false;
        }
    }

    for (let count of myMap.values()){
        if (count !== 0){
            return false;
        }
    }

    return true;
    // console.log(myMap);
}

console.log(isAnagram('Chigerish', 'Chigerish'));