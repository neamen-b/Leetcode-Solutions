/**
 * Initial thoughts
 *  Just use sum operation to get normal sum
 * For each number, use integer divison to extract digits for summation
 */

/**
 * @param {number[]} numbers
 * @return {number}
 */

function differenceOfSum(numbers : number[]) : number {
    //      var name         red funct   paramss  sum += curr   start sum
    const normal_sum : number = numbers.reduce((acc, curr) => acc + curr, 0);
    var digit_sum : number = 0;

    for(const num of numbers){
        let quotient : number = num;
        while (quotient != 0){
            // Extracts 10th place digit
            digit_sum += quotient % 10;
            quotient = Math.floor(quotient / 10);
        }
    }

    return Math.abs(normal_sum - digit_sum);
}


function test (func : Function, tests : number[][]) : void{
    for (let nums of tests){
        console.log(func(nums));
    }
}

const tests = [[1,15,6,3], [1,2,3,4]];
test(differenceOfSum, tests);