// =============================
//  ROMAN NUMERAL QUIZ GAME
// =============================
function romanToDecimal(roman) {
    const romanValue ={
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
const rangeValue = roman.length;
let result = 0;
    for (let i = 0; i < rangeValue; i++) {
        if (i < rangeValue-1 && romanValue[roman[i]] < romanValue[romanValue[i+1]]) 
            {
            result += romanValue[roman[i+1]] - romanValue[roman[i]];
            i++;
        } else {
            result += romanValue[roman[i]];
        }
}
}
function getRandomRoman() {
    let romans = [
        "I","II","III","IV","V","VI","VII","VIII","IX","X",
        "XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX"
    ];
    const index = Math.floor(Math.random() * romans.length);
    return romans[index];
}

function startQuiz(rounds) {
    let score = 0;
    for (let j = 1; j < rounds; j++) {
        console.log(`Round ${j}`);
        let roman = getRandomRoman();
        console.log(`Convert this roman numerial to desimal : ${roman}`);
        let answerText = "Please enter your answer here!";
        let answer = parseInt(answerText);
        let correct  = romanToDecimal(roman);
            if (answer === correct) {
                console.log("Correct");
                score++;
            } else {
                console.log(`Wrong! your correct answer ${correct}`);
            }
    }
    console.log(`Quiz finished! Your total score: ${score}/${rounds}`);
    
}

// =========================
// #### TESTING PROGRAM ####
// =========================
startQuiz(10);

