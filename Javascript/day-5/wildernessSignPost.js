/*
    Create a function named createSignpostMessage that receives distance and landmark as its parameters.

    This function aims to create a message for a signpost during a hike in the wilderness. The message should guide hikers to a scenic viewpoint by specifying the distance and describing the landmark.
    The message should be formatted as follows:
    "Follow the trail for {distance} miles to the {landmark}."
    where {distance} is the numeric distance value and {landmark} is the description of the landmark.

    For example, if the distance is 2 and the landmark is "Majestic Waterfall", the function should return:
    "Follow the trail for 2 miles to the Majestic Waterfall."

    Make sure to use the provided distance and landmark values in the formatted message.

    Parameters:

    distance (integer): The distance, in miles, to the scenic viewpoint.
    landmark (string): A description of the landmark or scenic viewpoint.
    The function returns a string containing the formatted signpost message.
*/

function createSignpostMessage(distance,landmark) {
    return `Follow the trail for ${distance} miles to the ${landmark}.`
}
console.log(createSignpostMessage(80,"Merbabu Mountain"));