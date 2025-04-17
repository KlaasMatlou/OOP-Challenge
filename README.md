# Virtual Pet in Python

This project implements a simple virtual pet using Python, demonstrating basic object-oriented programming principles. The code is structured into two main files for better organization.

## Features

* **Pet Class (pet.py):** Defines the Pet class with attributes like name, hunger, energy, and happiness. It also includes methods for actions such as eating, sleeping, playing, getting status, training, and showing tricks.
* **Main Interaction (main.py):** Contains the main script that imports the Pet class and demonstrates how to create and interact with Pet objects.
* *Basic Pet Actions:*
    * **eat():** Simulates feeding, decreasing hunger and increasing happiness.
    * **sleep():** Simulates resting, increasing energy and slightly decreasing happiness.
    * **play():** Simulates playing, decreasing energy, increasing happiness, and slightly increasing hunger.
* *Status Display:* The get_status() method provides a clear overview of the pet's current condition.
* *Trick Training (Bonus):* The train(trick) method allows teaching the pet new tricks, stored in a list.
* *Show Tricks (Bonus):* The show_tricks() method displays the list of learned tricks.

## Getting Started

1.  *Save the code:*
    * Save the Pet class definition in a file named pet.py.
    * Save the main interaction script (that creates and uses Pet objects) in a file named main.py in the *same directory*.

2.  *Run the main script:* Open your terminal or command prompt, navigate to the directory where you saved the files, and execute the main.py script using:

    bash
    python main.py
    

    This will run the example interactions defined in main.py.

## File Structure
