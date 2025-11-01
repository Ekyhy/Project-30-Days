// To do task :
/* 
    Create a function named aquaticSpeciesObservation that receives river, species, and time as its parameters

    The function should generate an observation report for a nature enthusiast's to observe unique aquatic life forms
    in a primitive river ecosystem. It will concatenate the input
    parameters to form a detailed observation string and compare it with a predefind rare sighting condition.

    Follow these steps to implement the function:
        1. Concatenate the inputs to create an observation string in the format: "Observed [species] in [river] at [time]".
        2. Compare the create observation string with the predefind rare sighting condition: "Observed axolotl in Amazon River at midnight".
        3. if the observation matches the rare sighting condition, return "Rare species sighted!".
        4. if nor, return the concatenated observation string.

    Hint, parameters!!
        river (string): The name of the river where the observation took place.
        species (string): The name of the aquatic species observed.
        time (string): The time of the observation.
*/

// Create a function named aquaticSpeciesObservation using three parameters
function aquaticSpeciesObservation(river,species,time){
    // Concatenated the input observation using variable const name observation, in this case we are using {``} (backtick)
    const observation = `Observed ${species} in ${river} at ${time}`;
    // Create condition rareSighted
    const rareSighted = "Observed axolotl in Amazon River at midnight";

    // Make to condition using if condition to compare two variable observation and raresighted

    if(observation === rareSighted){
        // if condition result true, return value "Rare species sighted";
        return "Rare species sighted!";
    } else {
        // if condition result false, return start state variable obsevation
        return observation;
    }
}