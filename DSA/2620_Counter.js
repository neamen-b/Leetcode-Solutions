/**
 * @param {number} n
 * @return {Function} counter
 */


let createCounter = function(n){

    let current_val = n;

    function add(){
        // current_val = current_val + 1;
        return current_val++;
    }

    return add;
}

const counter = createCounter(10);

for (let index = 0; index < 10; index++) {
    console.log(counter());
}