/*
====================================================================================================
    Arrays are collections of items created using square brackets [] with items separated by commas:
    let myArray = [1, 2, "three", true];
    To get the length of an array, use the length property:
    let length = myArray.length; 
=====================================================================================================
Accessing Array Elements
    Arrays store multiple values in a single variable. Each element has an index starting from 0:

    let myArray = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    Access elements using square brackets with the index:

    let myArray = [10, 20, 30, 40, 50]
    let element = myArray[2] // Returns 30
    Iterate over arrays using .length property:

    for (let i = 0; i < myArray.length; i++) {
        console.log(myArray[i]);
    }
==================================================================================================
*/

// Create an array called shoppingList that contains the following items: bread, eggs, milk, and butter.
// Output the array in the end.

let shoppingList = ["bread","eggs","milk","butter"];
console.log(shoppingList);

// Create a function named values that receives an array as an argument and prints all of the items in the array one after the other.

function values(arr) {
    for (let i = 0; i < arr.length; i++) {
        const element = arr[i];
        console.log(element);
    }
}

console.log(values[1,2,3,2,1]);
