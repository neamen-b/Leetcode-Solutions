/**
 * Initial thoughts
 *  Just use sum operation to get normal sum
 * For each number, use integer divison to extract digits for summation
 */
/**
 * @param {number[]} numbers
 * @return {number}
 */
function differenceOfSum(numbers) {
    //      var name         red funct   paramss  sum += curr   start sum
    var normal_sum = numbers.reduce(function (acc, curr) { return acc + curr; }, 0);
    var digit_sum = 0;
    for (var _i = 0, numbers_1 = numbers; _i < numbers_1.length; _i++) {
        var num = numbers_1[_i];
        var quotient = num;
        while (quotient != 0) {
            // Extracts 10th place digit
            digit_sum += quotient % 10;
            quotient = Math.floor(quotient / 10);
        }
    }
    return Math.abs(normal_sum - digit_sum);
}
function test(func, tests) {
    for (var _i = 0, tests_1 = tests; _i < tests_1.length; _i++) {
        var nums = tests_1[_i];
        console.log(func(nums));
    }
}
var tests = [[1, 15, 6, 3], [1, 2, 3, 4]];
test(differenceOfSum, tests);
