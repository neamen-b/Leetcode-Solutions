/**
 * ListNode Definiton
 */
/**
 * 
 * @param {Number} val 
 * @param {ListNode} next 
 */
function ListNode(val, next){
    this.val = (val === undefined? undefined : val );
    this.next = (next === undefined? undefined : next)
}

/**
 * @param {Number} val1
 * @param {Number} val2
 * @return {Number} 
 */

var gcd = function (val1, val2){
    while(val2 !== 0){
        let temp = val2;
        val2 = val1 % val2;
        val1 = temp;
    }
    return val1;
}

/**
 * @param {ListNode} head
 * @return {ListNode} 
 */

var insertGCD = function(head){

    // If the list is empty or if there is only one node. Cannot insert in between
    // if (head === undefined || head.next === undefined){
    //     return null
    // }
    // Actually it is guaranteed that there is at least one head
    // Also instead of undefined, it deafults to null
   // If the list is empty or if there is only one node. Cannot insert in between
   if (head.next === null){
    return head
    }
    var current_node = head;

    while (current_node !== null){

        if (current_node.next !== null){
            let new_node = new ListNode(gcd(current_node.val, current_node.next.val));
            // console.log("sett new.next to", current_node.next.val);
            new_node.next = current_node.next;
            // console.log("current node rn ", current_node.val)

            // console.log("setting current_node.next to ", new_node.val);
            current_node.next = new_node;
            // console.log(current_node.val, new_node.val, current_node.next.next.val);
            current_node = current_node.next.next;

        }  else{

            return head;
        }
    }
}

let A = new ListNode(21);
let C = new ListNode(7);
let B = new ListNode(8,C);
A.next = B;

console.log(insertGCD(A));
let curr = A;
while (curr){
    console.log(curr.val);
    curr = curr.next;
}