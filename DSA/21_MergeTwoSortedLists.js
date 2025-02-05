/**
 * List node defintion
 * @param {number} val
 * @param {ListNode} next
 */


function ListNode(val, next){
    this.val = val === undefined ? null : val;
    this.next = next === undefined ? null : next;
}


/**
 * @param {ListNode} head1
 * @param {ListNode} head2
 * @return {ListNode}
 */


let mergeTwoLists = function(head1, head2){


    if (head1 === null && head2 !== null){
        return head2;
    }
    else if (head1 !== null && head2 === null){
        return head1;
    } 

    if (head1 === null && head2 === null){
        return head1;
    }
    // Merged linked list head
    let merge_head = undefined;

    // Pointers to the element of the two linked lists
    let current_node1 = undefined;
    let current_node2 = undefined;

    // Set the head of the merged list, head1 is selected if equal
    // Set the current nodes accrodingly
    if (head1.val <= head2.val){
        merge_head = head1;
        current_node1 = head1.next;
        current_node2 = head2;
    } else {
        merge_head = head2; 
        current_node1 = head1;
        current_node2 = head2.next;
    }
    // "pointers"
    console.log(`Initial Merge Head = ${merge_head.val} ${merge_head.next.val}`);
    let last_node_added = merge_head;
    // While either list1 or list2 has defined nodes
    while(current_node1 || current_node2){

        if(current_node1 === undefined || current_node1 === null){
            last_node_added.next = current_node2;
            return merge_head;
        }
        else if (current_node2 === undefined || current_node2 === null){
            last_node_added.next = current_node1;
            return merge_head;
        }

        if(current_node1.val <= current_node2.val){
            last_node_added.next = current_node1;
            last_node_added = current_node1;
            current_node1 = current_node1.next;
        }
        else{
            last_node_added.next = current_node2;
            last_node_added = current_node2;
            current_node2 = current_node2.next;
        }

        console.log(`last node added -> ${last_node_added.val}`);
    }
}

// Test  lists
/**
 *  1 -> 4 -> 8 -> 9
 * 
 *  1 -> 3 -> 4
 */
let list1_head = new ListNode(1);
let list2_head = new ListNode(1);
let list1_4 = new ListNode(4);
let list1_8 = new ListNode(8);
let list1_9 = new ListNode(9);

let list2_3 = new ListNode(3);
let list2_4 = new ListNode(4);

list1_head.next = list1_4;
list1_4.next = list1_8;
list1_8.next = list1_9;
list2_head.next = list2_3;
list2_3.next = list2_4;

// node = mergeTwoLists(list1_head, list2_head);

// while(node){
//     console.log(node.val);
//     node = node.next;
// }




/**
 * @param {ListNode} head1
 * @param {ListNode} head2
 * @return {ListNode}
 * 
 * Recursive solution
 */


let MergeTwoLists = function (head1, head2){

    if (head1 === null && head2 !== null){
        return head2;
    }
    else if (head1 !== null && head2 === null){
        return head1;
    }
    else if (head1 === null && head2 === null){
        return head1;
    }

    

}

MergeTwoLists(list1_head, list2_head);
