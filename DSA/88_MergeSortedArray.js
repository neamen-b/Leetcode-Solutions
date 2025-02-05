/**
 * Initial thoughts:
 *      Use two pointers to traverse the arrays and order them in num1
 *      I will need to copy num1 for this approach
 * 
 *      copy = nums1
 *      
 *      Two pointers
 *      i = 0
 *      j = 0
 * 
 *      Length of num1 = m
 *      length of num2 = n
 * 
 *      shortest = m or n
 *      
 *       while (i < m or  j < n){
 *  
 *         }
 *          
 *      
 */



/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} m
 * @param {number} n
 * @return {void}
 * 
 * Two pointers and a copy of num1 approach
 */

let merge = function(nums1, m, nums2, n){

    if(m === 0  && n === 0){
        return nums1;
    }
    // copying nums1. O(n)
    let nums1_copy = nums1;

    // n1 -> nums1_copy pointer, n2 -> nums2 pointer, pos -> nums1 pointer
    let n1 = 0,  n2 = 0,  pos = 0;

    while(n1 < m || n2 < n){
        if(nums1_copy[n1] < nums2[n2]){
            nums1[pos] = nums1_copy[n1];
            pos++;
            n1++;
        }
        else{
            nums1[pos] = nums2[n2];
            pos++;
            n2++;
        }
        console.log(n1,n2);
    }

    console.log(nums1);
}


let nums1 = [1,3,5,8,0,0,0,0];
let nums2 = [3,4,4,6];


merge(nums1, 4, nums2, nums2.length);