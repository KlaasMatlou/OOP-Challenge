# Virtual Pet in Python

This project implements a simple virtual pet using Python, demonstrating basic object-oriented programming principles. The pet has attributes and can perform actions to simulate interaction.

## Features

* *Pet Attributes:* Each pet has a name and tracks its levels of hunger, energy, and happiness. These are initialized when a new pet is created.
* *Basic Actions:*
    * **eat():** Simulates feeding the pet, which decreases its hunger and increases its happiness.
    * **sleep():** Simulates the pet resting, increasing its energy and slightly decreasing its happiness.
    * **play():** Simulates playing with the pet, decreasing its energy, increasing its happiness, and slightly increasing its hunger.
* *Status Display:* The get_status() method provides a clear overview of the pet's current hunger, energy, and happiness levels.
* *Trick Training (Bonus):* The train(trick) method allows you to teach the pet new tricks, which are stored in a list associated with the pet.
* *Show Tricks (Bonus):* The show_tricks() method displays the list of tricks the pet has learned.

## Getting Started

1.  *Save the code:* Save the provided Python code for the Pet class in a file named pet.py. This file contains the blueprint for creating pet objects and their behaviors.
2.  *Run the script:* You can run the pet.py file directly using the Python interpreter. The end of the file includes an example of creating a Pet object and interacting with it.

    bash
    python pet.py
    

## How to Use

To use the Pet class in your own Python code:

1.  *Import the class:* Import the Pet class from the pet.py file.
2.  *Create an object:* Instantiate the Pet class to create a new virtual pet, providing a name for it.
3.  *Interact with the pet:* Call the various methods of the Pet object (e.g., eat(), sleep(), play(), get_status(), train(), show_tricks()) to simulate actions and check its current state.

## Example Usage (Conceptual)

The pet.py file includes an example of creating a pet named "Thabo" and demonstrating how to use the different methods to interact with it, such as checking its initial status, feeding it, playing with it, checking its status again, teaching it a trick, and showing its learned tricks. Running the script will output the results of these actions.

## Further Development

This project provides a basic foundation for a virtual pet. Potential extensions include adding more attributes, implementing more complex interactions, adding persistence (saving and loading pet data), or creating a user interface for a more interactive experience.
