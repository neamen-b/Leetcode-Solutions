/**
 * Collect odd and even separately, then connect odd to even list
 */


// Listnode class with constructor

interface ListNode{
    // declare instace attributes here
    val : number | null | undefined;
    next : ListNode | null | undefined;

    show() : void;
}
class ListNode implements ListNode{
    // for creating an instance of ListNode with values assigned
    constructor(val : number | null | undefined, next : ListNode | null | undefined){
        this.val = val != null ? val : undefined;
        this.next = next != null ? next : undefined
    }

    show() : void{
        if (this.val != undefined && this.next != undefined){
            console.log(` Val = ${this.val} , Next ${this.next.val}`)
        }
        else if (this.val != undefined && this.next == undefined){
            console.log(`Val = ${this.val}, Next = ${this.next}`)
        }
        else {
            console.log("Null Node")
        }
    }


}

function OddEvenLinkedList(head : ListNode) : ListNode{

    if (head === null || head.next === null){
        return head;
    }
    var odd = head
    var even_head = head.next
    var even = head.next

    while (even != null && even.next != null){
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
    }
    odd.next = even_head;
    return head
}


const odd_length_list : ListNode = new ListNode(1, new ListNode(2, new ListNode(3, null)))
const even_length_list : ListNode = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, null))))
const lists : Array<ListNode> = [odd_length_list, even_length_list]

function test(lists : Array<ListNode>) : void {
    for (const head of lists){
        var new_head = OddEvenLinkedList(head);
        var curr = new_head;
        while(curr != null){
            curr.show()
            curr = curr.next
        }
    }
}

test(lists);