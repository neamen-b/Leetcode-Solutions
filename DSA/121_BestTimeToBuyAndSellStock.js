/**
 * initiala thoughts
 *
 *  left min
 * and right max
 * go inwards
 * then calculate difference of max and min
 *
 *
 * Second attempt
 *
 *  keep going with both start and end until the ends of the array.
 *  if val is less than min and indexof val is <= than index of max
 *      min = val
 *  else if
 *      val is >= max and indexof val is >= index of min
 *        max = val
 *
 * Third attempt
 * Apparently a two-pointer approach was not the best approach here.
 *  I kept getting min after the max , or max  before mins
 *  Two pointer approaches are best for monotonic sequences (increasing or decreasing, sorted. )
 *
 * so a one pass approach is better here lowest price is kep track of.
 */
/**
 * @param {number[]}  prices
 * @return {number}
 *
 * Does not work when if the max or min is beyond where the loop terminates
 */
function MaxProfit(prices) {
    var min = Infinity;
    var max = -Infinity;
    var start = 0;
    var end = prices.length - 1;
    while (start <= end) {
        console.log("start ".concat(prices[start], ", end ").concat(prices[end], ", s ").concat(start, " e ").concat(end, " "));
        if (prices[start] < min) {
            min = prices[start];
        }
        if (prices[end] > max) {
            max = prices[end];
        }
        console.log("min ".concat(min, ", max ").concat(max));
        start++;
        end--;
    }
    var profit = max - min;
    return min - min > profit ? min - min : profit;
}
// console.log(MaxProfit([3,2,6,5,0,3]))
/**
 * @param {number[]} prices
 * @return {number}
*/
function MaxProfit2(prices) {
    var start = 0;
    var end = prices.length - 1;
    var min_val = [Infinity, start];
    var max_Val = [-Infinity, end];
    // var profits : number[] = new Array();
    while (start < prices.length) {
        console.log("start ".concat(prices[start], ", end ").concat(prices[end], ", s ").concat(start, " e ").concat(end, " "));
        if (prices[start] < min_val[0] && start <= max_Val[1]) {
            min_val = [prices[start], start];
        }
        if (prices[end] > max_Val[0] && end >= min_val[1]) {
            max_Val = [prices[end], end];
        }
        console.log("min ".concat(min_val[0], ", max ").concat(max_Val[0]));
        start++;
        end--;
        // profits.push(max_Val[0] - min_val[0])
    }
    // console.log(profits);
    // console.log(Math.max(...profits));
    return max_Val[0] - min_val[0];
}
// console.log(MaxProfit2([2,7,1,4]))
/**
 *  One pass Dp
 *  going from the left to the right, keep track of the smallest.
 *  caluclate the potential profit at each index, if > max_profit, set to max_profit
*/
/**
 * @param {number[]} prices
 * @return {number}
*/
function MaxProfit3(prices) {
    var lowest_price = Infinity;
    var max_profit = -Infinity;
    for (var i = 0; i < prices.length; i++) {
        lowest_price = Math.min(lowest_price, prices[i]);
        max_profit = Math.max(max_profit, prices[i] - lowest_price);
    }
    return max_profit;
}
console.log(MaxProfit3([2, 7, 1, 4]));
