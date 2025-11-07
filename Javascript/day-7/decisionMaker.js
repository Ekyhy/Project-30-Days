function subathing(temperature,spiderCount) {
    if (spiderCount >= 3) {
        return "Find another spot!"
    } else if (spiderCount > 0) {
        return "Be cautious!"
    } else if (temperature < 25) {
        return "Too cold!"
    } else if (temperature > 30) {
        return "Too hot!"
    } else {
        return "Perfect spot!"
    }
}


console.log(subathing(26,1));
console.log(subathing(30,0));
console.log(subathing(18,0));
console.log(subathing(31,0));
console.log(subathing(28,4));




