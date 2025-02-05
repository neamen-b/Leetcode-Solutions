/**
 * Inital Thoughs:
 *      Binary Search but to find the first occurence. Minimizes API calls by having the potential calls each time
 *      Since the all the versions after the first occurence are all bad, we can look in the left half of the array
 *      
 *      start = 0
 *      mid = (len(versoin) - 1) // 2
 *      end = len(version) - 1
 *      
 *      While mid <= end
 *      Is badversion(version[mid]) bad?
 *          Yes: Look in left half , end = mid
 *          No: look in right half, start = mid
 * 
 * 
 * 
 */

/**
 * @param {Array} Arr
 * @return {Integer}
 *

var Solution = function (Arr) {

    // start = 0
    // // Integer Division
    // end = Arr.length - 1

    // Binary Search the first occurence of bad
    return function searchFirst(start, end, Arr) {
        // If array is empty, then no bad version.
        if (Arr.length === 0) return null;

        // If array has only one element, return element if bad
        if (start == end) {
            return (Version[Arr[start]] == 'Bad') ? Arr[start] : null;
        };
        // console.log(`start = ${start}, end = ${end}`)

        // when array section down to adjacent indices
        if (start == (end - 1)) {
            // If they are both bad, return the one that comes first
            if (Version[Arr[start]] == 'Bad' && Version[Arr[end]] == 'Bad') {
                // console.log('Adjacent')
                return Math.min(Arr[start], Arr[end]);
            };

            // If they are both Good, return null
            if (Version[Arr[start]] == 'Good' && Version[Arr[end]] == 'Good') {
                // console.log('Adjacent')
                return null
            };

            // If only one of them is bad, return the bad one
            return (Version[Arr[start]] == 'Bad') ? Arr[start] : Arr[end];

        };

        // Calculate the mid. Integer division
        mid = Math.floor((start + end) / 2);
        // console.log(`Mid_index = ${mid}, Mid_val = ${Arr[mid]}`)



        if (Version[Arr[mid]] == 'Bad') {
            end = mid - 1;
            // console.log(` BAD - Going to my left, end = ${end}`)
            // console.log('-----------------------------')
            return searchFirst(start, end, Arr)
        }
        if (Version[Arr[mid]] == 'Good') {
            start = mid + 1;
            // console.log(` GOOD - Going to my right, end = ${end}`)
            // console.log('-----------------------------')
            return searchFirst(start, end, Arr);
        };
    };

};

// This is my record of versions and their status for testing
Version = { 2: "Good", 1: "Bad", 3: "Bad", 4: "Bad", 5: "Bad" };

// Version numbers
n = [3,5,2,1,4];

console.log(Solution(n)(start = 0, end = n.length - 1, n));
*/


// Solution to be submitted
/**
 * Definition for isBadVersion()
 * 
 * @param {integer} version number
 * @return {boolean} whether the version is bad
 * isBadVersion = function(version) {
 *     ...
 * };
 */


/**
 * @param {function} isBadVersion()
 * @return {function}
 */
var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
     
    return function(n) {
        let Version = []

        // Array of Version for binary search
        // Heap out of memory for large instances of n - No good
        for (let index = 1; index <= n; index++) {
            Version.push(index)
        }

        function search(start, end, Version){

            // If Version empty or null, return null
            if (Version.length == 0 || !Version) return null;

            // If version has only one element, return element if Bad
            if (start == end){
                // If version is bad, return version, else null
                return isBadVersion(Version[start]) ? Version[start] : null;
            };

            // If adjacent indices
            if (start == (end - 1)) {

                // If both bad, return whichever comes first
                if (isBadVersion(Version[start]) == true && isBadVersion(Version[end]) == true){
                    return Math.min(Version[start], Version[end]);
                };
                
                // if both good, return null
                if (isBadVersion(Version[start]) == false && isBadVersion(Version[end]) == false){
                    return null;
                };

                // If either bad, return the bad
                return isBadVersion(Version[start]) == true ? Version[start] : Version[end];
            };

            mid = Math.floor((start + end) / 2);

            // If version is bad, look left half
            // Do not remove Versoin[mid] becasue it could be the first bad
            // So end = mid instead of mid -1 
            if (isBadVersion(Version[mid]) == true){
                end = mid;
                return search(start, end, Version);
            }
            // If version is good, look in right half
            // If good, we can remove it because we do not care for it
            else {
                start = mid + 1;
                return search(start, end, Version);
            };
        };
        return search(0, Version.length - 1, Version);
    };
};



var solution = function(isBadVersion) {
    /**
     * @param {integer} n Total versions
     * @return {integer} The first bad version
     */
    
    function search(start, end){

        if (start >= end){
            return start;
        };

        mid = Math.floor((start + end) / 2);

        if (isBadVersion(mid)){
            return search(start, mid);
        }
        else {
            return search(mid + 1 , end)
        }
    }
    return function(n) {
        return search(1,n)
    };
};
