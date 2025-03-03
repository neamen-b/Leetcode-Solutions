/**
 * Initial thoughts
 *  keep track of the number of elements that you have left
 *   if it is ever lower than the amount of coins that need to be placed, stop
 *  
 */

/**
 * @param {number} n
 * @return {number}
 */

function arrangCoins(n: number): number{
    var coins_left : number = n;
    var complete_row_count : number = 0;
    var row_size : number = 1;

    while(row_size <= coins_left){
        complete_row_count++;
        coins_left = coins_left - row_size;
        row_size++;
    }
    return complete_row_count;
}


function test(numbers : number[], func : Function) : void{
    for (let num of numbers){
        console.log(func(num));
    }
}

var tests : number[] = [5, 8];

/**
 * 
 * @param {number} n
 * @return {number}
 * Binary Search Approach using Gauss' Summation Formula
 */
function arrangeCoins2 (n : number) : number{
    // coins = 1 + 2 + 3 ..... k <= n
    // coins = (k(k+1)) / 2, gives the sum of the first k rows
    // What is the largest k where coins <= n?

    var start : number = 0;
    var end : number = n;
    // var k : number = -1;

    while (start <= end){
        var k = Math.floor((start + end) / 2);
        var coins = Math.floor((k * (k + 1)) / 2);
        console.log(`start ${start} , end ${end} , k ${k}, ${coins}, ${n}`)
        if (coins == n){
            return k;
        }
        else if (coins > n){
            end = k - 1;
        }
        else{
            start = k + 1;
        }
    }
    return end;
    
}
test(tests, arrangeCoins2);