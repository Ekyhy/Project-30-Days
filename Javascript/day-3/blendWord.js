// To do Task :
/*
    Create a function named blendWords that receives word1 and word2 as parameters.
    This function concatenates the two words, omitting one of the duplicate letters if the last letter of word1 and the first letter of word2 are the same.

    Handle the following cases:
    If the last letter of word1 and the first letter of word2 are the same, omit one of the duplicate letters.
    If either word1 or word2 is empty, return the non-empty string.
    If both are empty, return an empty string.
    Parameters:

    word1 (string): The first word.
    word2 (string): The second word.
    Returns a string, the result of blending word1 and word2.
*/

function blendWords(word1,word2){
    // first 1 : make a condition if word1 and word 2 is empty
    if (word1 === '' && word2 === '') {
        return '';
    }
    // Second : make a condition if one between word1 or word 2 is a empty
    if (word1 === '') {
        return word2;
    }
    if (word2 === '') {
        return word1;
    }
    // take a last character from word1 and decrease 1
    const lastChar = word1[word1.length-1];
    // teke a first character from word 2 
    const firstChar = word2[0];
    // Third : Compare between lastChar and firstChar to combine them without repeating the same character
    // last char in word 1 and first char in word 2
    // for example : code edior === codeditor
    if (lastChar === firstChar) {
        return word1+word2.slice(1);
    }
    // Four: If different Combine first
    return word1+word2;
}