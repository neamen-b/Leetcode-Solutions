/**
 * Initital thoughts:
 * 
 *      Two 2D arrays where, items = [[value, weight]]
 * 
 *      1. Using a hashtable
 *          key (value)
 *          values( weight)
 * 
 *        add the first array into a hashtable with keys as values and values as weights
 * 
 *         for pair in items2:
 *              if pair[0] in hashtable:
 *                    increment weight
 *              else
 *                     add to table
 *         
 *          Now, how can I sort it while doing this?
 */


/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 * */

let mergeSimilarItems = function (items1, items2){

    // value -> weight hash table
    // neat way of creating a map from a 2d array
    // each inner array is treated a a key value pair
    let myHash = new Map(items1);
    
    for (pair of items2){
        
        if(myHash.has(pair[0])){
            myHash.set(pair[0], myHash.get(pair[0]) + pair[1]);
        }
        else{
            myHash.set(pair[0],pair[1]);
        }
    }
    console.log(myHash);
    let arr = [];
    for (pair of myHash.entries()){
        arr.push(pair);
    }

    return arr.sort((a,b) => a[0]-b[0]);
}

// Testing and learning
mergeSimilarItems([[1,2],[3,4],[2,3]], [[1,2],[2,3],[3,4]]);