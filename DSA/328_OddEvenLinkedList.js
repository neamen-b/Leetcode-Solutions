/**
 * Collect odd and even separately, then connect odd to even list
 */
var ListNode = /** @class */ (function () {
    // for creating an instance of ListNode with values assigned
    function ListNode(val, next) {
        this.val = val != null ? val : undefined;
        this.next = next != null ? next : undefined;
    }
    ListNode.prototype.show = function () {
        if (this.val != undefined && this.next != undefined) {
            console.log(" Val = ".concat(this.val, " , Next ").concat(this.next.val));
        }
        else if (this.val != undefined && this.next == undefined) {
            console.log("Val = ".concat(this.val, ", Next = ").concat(this.next));
        }
        else {
            console.log("Null Node");
        }
    };
    return ListNode;
}());
function OddEvenLinkedList(head) {
    if (head === null || head.next === null) {
        return head;
    }
    var odd = head;
    var even_head = head.next;
    var even = head.next;
    while (even != null && even.next != null) {
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
    }
    odd.next = even_head;
    return head;
}
var odd_length_list = new ListNode(1, new ListNode(2, new ListNode(3, null)));
var even_length_list = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, null))));
var lists = [odd_length_list, even_length_list];
function test(lists) {
    for (var _i = 0, lists_1 = lists; _i < lists_1.length; _i++) {
        var head = lists_1[_i];
        var new_head = OddEvenLinkedList(head);
        var curr = new_head;
        while (curr != null) {
            curr.show();
            curr = curr.next;
        }
    }
}
test(lists);
