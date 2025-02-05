/**
 * @param {Object | Array} obj
 * @return {boolean}
 * 
 */

//  Can assign functions to varaibles in JS
//  The variable references the function. Can use variable to invoke function
// This means that functions can be stored in data structures
//  Imagine having an array of functions
// Also known as an anonymous function since it does not have a name

var isEmpty = function(obj){

    // If array length is 0, then empty
    // Haha, obj.length might pull out a property so this is mihgt fail
    // if (obj.length === 0){
    //     console.log('length = 0')
    //     return true

    // If empty
    if (!obj){
        return true

        // If object is null, then empty
    } else if (obj === null){
        console.log('obj = null')
        return true
        // If object is undefined, then empty
    } 
    // The keys of an object habe a length attribute though. So if keys array.length is 0, empty
    else if (Object.keys(obj).length === 0){
        return true
    }

    // This is no good because an object does not have a length atrribute.
    // else if (obj.length === undefined){
    //     console.log('length = undefined')
    //     return true
    else {
        return false
    }
}

var obj = []
console.log(isEmpty(obj))
// console.log(typeof(obj))