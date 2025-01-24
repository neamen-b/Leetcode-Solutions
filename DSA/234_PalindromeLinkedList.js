/**
 * Initial thoughts:
 *  
 *  Use a stack to store values going from head to tail
 *      1. By popping each one, I get the values in reverse order
 *      2. By concatenating the stack, implemented with a list, get the og string and compare
 *  
 */



/**
 * Definition of a List Node
 * Default values for attributes assigned if nothing is passed to the constructor
 */

function ListNode(val = 0, next = null){
    this.val = val;
    this.next = next;

    // Automatically returns this which is bound to the object created
    // return this;
}


let isPalindrome = function (head) {
    // If head is null or undefined , return false
    // Don't think null or undefined counts as palindrome 
    if (head === null || head === undefined){
        return false;
    }

    // stack for keeing, LIFO
    let reverse_stack = [];
    let node = head;

    // While not null
    while (node !== null && node !== undefined){
        // console.log(node.val);
        reverse_stack.push(node.val);
        node = node.next;
    
    }

    start = 0;
    end = reverse_stack.length - 1;

    while (start <= end){
        if (reverse_stack[start] !== reverse_stack[end]){
            return false;
        }
        start += 1;
        end -= 1;
    }

    return true;
}


let A = new ListNode(1);
let B = new ListNode(2);
let C = new ListNode(2);
let D = new ListNode(1);

// console.log(A.val, B.val)

A.next = B;
// B.next = C;
// C.next = D;
console.log(isPalindrome(A));