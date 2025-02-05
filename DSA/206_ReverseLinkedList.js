/**
 * While node is not nul
 *      prev  = node
 *      node.next.next = node 
 * 
 * Let's do this the easy way first
 */

/**
 * Tree node ndefiniton
 */
function ListNode(val, next){
    this.val = (val === undefined? 0 : val)
    this.next = (next === undefined? null: next)
}
// C = new ListNode(3)
B = new ListNode(2)
A = new ListNode(1,B)

/**
 * @param {ListNode} head
 * @return {ListNode}
 */

var reverseList = function(head){

    // Empty list cannot be reversed
    if (head === null){
        return null;
    }
    // Single node list is the same reversed
    if(head.next === null){
        return head;
    }
    var new_nodes = [];
    var curr = head;

    while (curr !== null){
        // console.log(curr)
        new_nodes.push(curr);
        curr = curr.next;
    }
    // console.log(new_nodes);
    var current;

    new_head = new_nodes[new_nodes.length-1];

    while (new_nodes.length !== 0){
        if (new_nodes.length > 1){
            current = new_nodes.pop()
            prev = new_nodes.pop()
            // console.log(current, prev)
            current.next = prev;
            new_nodes.push(prev);
        } else{
            new_nodes.pop().next = null;
        }
    }
    return new_head;
}
console.log(reverseList(A));