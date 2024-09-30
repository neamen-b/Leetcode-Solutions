/**
 * Intitial thoughts?
 *      Thought of doing BFS and return true if any path summed to k but it doesn't work because the elements 
 *      don't have to be connected
 * 
 *      Alternative:
 *      
 *       Store values in a hash set and see if each node has a complement
 * 
 *      for each node:
 *          if k - node is set:
 *              return true
 *      return false
 */


/**
 * TreeNode definition
 * @param {number} val
 * @param {TreeNode} left
 * @param {TreeNode} right
 */


function TreeNode(val, left, right){
    this.val = val === undefined ? 0 : val;
    this.right = right === undefined ? null : right;
    this.left = left === undefined ? null :left;
}


/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 * Hash Set approach
 */


let findTarget = function(root, k){

    // Mao to contain all the values , Node -> Value
    let myMap = new Map();

    // Helper function to traverse in order
    let inOrderTraverse = function(root){

        if (root === null || root === undefined){
            return;
        }
        // console.log(`where am i? ${root.val}`);
        if(root.left){
            inOrderTraverse(root.left);
        }
        myMap.set(root, root.val);

        if(root.right){
            inOrderTraverse(root.right);
        }
    }

    inOrderTraverse(root);

    for (node of myMap.keys()){
        // console.log(node);
        // console.log('----------');
        if(myMap.has(k - node) && myMap.size > 1){
            return true;
        }
    }

    return false;
    // console.log(mySet);
}

A = new TreeNode(5);
B = new TreeNode(3);
C = new TreeNode(6);
D = new TreeNode(7);

A.left = B;
A.right = C;
B.left = D;


// console.log(findTarget(A, 8));

/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 * 
 * Two pointer approach
 */


let findTarget2 = function(root, k){

    // Holds numbers from inroder traversal
    let sorted_numbers = [];
    // Just for learning
    // A call stack to see how it is traversed
    let stack = [];
    // Helper function to travers
    function traverse(root){

        if(root === null || root === undefined){
            return;
        }
        // This is my made up call stack
        stack.push(root.val);

        if(root){
            traverse(root.left);
            sorted_numbers.push(root.val);
            traverse(root.right);
        }
    }

    traverse(root);

    console.log(`call stack ${stack}`);

    // Two pointers
    start = 0;
    end = sorted_numbers.length - 1;

    // until we are at the middle element
    // this workd because the in order traversal sorts
    while(start < end){
        // If sum of ends is < k, we need bigger nubmer so increment start
        if(sorted_numbers[start] + sorted_numbers[end] < k){
            start++;
        }
        // decrement end because we need smaller numbers 
        else if(sorted_numbers[start] + sorted_numbers[end] > k){
            end--;
        }
        else{
            return true;
        }
    }

    // console.log(sorted_numbers);
    return false;
}

// console.log(findTarget2(A,8));


/**
 * Iterative in order traversal
 * Just for practice
 */

let DFS = function(root){

    // Stack for traversal
    // Initialzed with root
    let stack = [root];

    // hold values from the sorted 
    let sorted_array = [];

    // Defining current node here because if created in the loop then it world create a new object each time
    let current_node = undefined;
    while(stack.length !== 0){
        current_node = stack.pop();
        
        if(current_node.right){
            stack.push(current_node.right);
        }
        if(current_node.left){
            stack.push(current_node.left);
        }

        sorted_array.push(current_node.val);
    }

    console.log(sorted_array);
    console.log(stack);
}

DFS(A);