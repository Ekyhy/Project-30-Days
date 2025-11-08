/*
Create a function named createGardenLabel that receives plantName, plantAge, and isFlowering as parameters.

This function generates a formatted label for a plant, including its name, age, and flowering status.

The label format:

"Plant: [plantName], Age: [plantAge] years, Flowering: [yes/no]"
Replace [plantName] with the plant's name, [plantAge] with its age, and [yes/no] with "yes" if isFlowering is true, or "no" if false.

Examples:

"Plant: Rose, Age: 3 years, Flowering: yes"
"Plant: Cactus, Age: 5 years, Flowering: no"
Parameters:

plantName (string): The plant's name.
plantAge (number): The plant's age in years (positive integer).
isFlowering (boolean): Indicates if the plant is flowering.
Returns a string representing the formatted garden label.
*/

function createGardenLabel(plantName,plantAge,isFlowering){
    return(`Plant: ${plantName}, Age: ${plantAge} years, Flowering: ${isFlowering? 'Yes':'No'}`);   
}


console.log(createGardenLabel("Rose",10,false));
console.log(createGardenLabel("jasmine",1,true));

