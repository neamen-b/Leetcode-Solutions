/**
 * Initial thoughts
 *  
 * creating a constructor function
 */


/**
 * @param {number} init 
 * @return {increment : Function , decrement : Function , reset : Function}
 */

// OOP Style
let createCounter = function (init){

    this.init = init;

    this.increment = function (){
        return this.init + 1;
    }

    this.decrement = function (){
        return this.init - 1;
    }

    this.reset = function(){
        return this.init;
    }

    return {increment : this.increment() , decrement: this.decrement() , reset: this.reset()};
}

// let obj = new createCounter(5);

// // console.log(obj.init);
// console.log(obj.increment);
// console.log(obj.decrement);
// console.log(obj.reset);


// Weird style
/**
 * @param {number} init
 * @return {increment : Funciton , decrement: Function, reset: Function}
 */



let createCounter2 = function(init){
    let current_var = init;
    function increment(){
        current_var = current_var + 1;
        return current_var;
    }

    function decrement(){
        current_var =  current_var - 1;
        return current_var;
    }

    function reset(){
        current_var = init;
        return current_var;
    }

    return {increment, decrement, reset};
}

let counter = createCounter2(5);

console.log(counter.increment());
console.log(counter.decrement());
console.log(counter.reset());