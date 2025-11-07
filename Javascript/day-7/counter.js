/*
    How to create an Object Counter
    method 1

    let object = {
        method1: function(arg1) {
            // some code
        },
        method2: function(arg2) {
            // some code
        }
    };
    return object
    method 2

    let object = new Object();
    object.method1 = function(arg) {
        // some code
    }
    object.method2 = function(arg) {
        // some code
    }
    return object
    How to create a function
    method 1

    functionNameOne: function(arg) => {
        // do something.. return something..
    }
    method 2

    functionNameOne(arg) {
        // do something.. return something..
    }
    method 3

    functionNameOne: (arg) => returnValue
    How to throw an error
    throw new Error("message");
*/

/*
=================== TASK =======================

Write a function expect that helps developers test their code. It should take in any value val and return an object with the following two functions.

toBe(val) accepts another value and returns true if the two values === each other. If they are not equal, it should throw an error "Not Equal".
notToBe(val) accepts another value and returns true if the two values !== each other. If they are equal, it should throw an error "Equal".

=================================== Answer==========================================================================================================
*/


var expect = function(val) {
    const originalValue = val;
    return{
        toBe : (newVal) =>{
            if(newVal !== originalValue){
                return("Not Equal")
            }else return true
        },
        notToBe : (newVal) =>{
            if(newVal === originalValue){
               return("Equal")
            }else return true
        }
    }
};

// ========= TESTING PROGRAM ===============
console.log("{To Be} :",expect(5).toBe(7));
console.log("{Not To Be} :",expect(5).notToBe(5));

