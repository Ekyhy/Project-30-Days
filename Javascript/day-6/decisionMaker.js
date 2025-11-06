function forestHikeDecision(weather, energyLevel, daylight) {
  if (energyLevel < 30) {
    return "Take a break";
  } else if (weather === "sunny" && energyLevel > 70) {
    return "Continue hiking";
  } else if (weather === "rainy" && !daylight) {
    return "Set up camp";
  } else if (weather === "foggy" && daylight) {
    return "Proceed with caution";
  } else {
    return "Assess the situation";
  }
}

console.log(forestHikeDecision("sunny",80,true));
console.log(forestHikeDecision("rainy",50,false));
console.log(forestHikeDecision("foggy",60,true));
console.log(forestHikeDecision("cloudy",90,false));
console.log(forestHikeDecision("sunny",25,true));
console.log(forestHikeDecision("rainy",80,true));