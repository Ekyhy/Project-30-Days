// To do task :
/* 
    Create a function named decimalToBinary that receives a positive integer number in base 10.
    The function will convert the decimal number to its binary equivalent and return the binary result
    as a string. Consider the following:

        - The input number will always be a positive integer
        - The function should return the binary equivalent of thr
        input as a string
        - To convert a decimal number to binary, repeadly divide the number
        by 2 and keep track of the remainders. The remainders in reverse order
        will give you the binary equivalent.
*/

// Hint binary base 2 as a number.
// I will can be create function to translate from number to string
// I can use [to.String(params)]
// Params a optional. To base to use must be an integer between 2 and 36

function decimalToBinary(number){
    // Create variable to save input users and tarnslate to string
    textToStringBinary = number.toString(2);
    return textToStringBinary;
}

function decimalToOctal(number){
    textToStringOctal = number.toString(8);
    return textToStringOctal;
}