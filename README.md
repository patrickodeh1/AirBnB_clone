# AirBnB Clone

This project is a simplified clone of the AirBnB platform, developed as part of the Alx School curriculum. The project covers various aspects of software development, including object-oriented programming, file storage, and command-line interface (CLI) interactions.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
- [File Storage](#file-storage)
- [Testing](#testing)
- [Authors](#authors)

## Description

The AirBnB clone project is divided into several stages, each focusing on different parts of the application. The current stage involves creating a basic command interpreter to manage the application's data model, which includes users, places, states, cities, amenities, and reviews.

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/AirBnB_clone.git

2. Navigate to the project directory:

    cd AirBnB_clone

Ensure you have Python3 installed on your system.

## Usage

The command interpreter (console.py) allows you to interact with the application's data model. You can create, show, destroy, update, and list objects.

Starting the Command Interpreter
To start the command interpreter, run:

./console.py
#### Commands
create: Creates a new instance of a class.

(hbnb) create <class_name>
Example:

(hbnb) create User
show: Shows the string representation of an instance based on the class name and id.


(hbnb) show <class_name> <id>
destroy: Deletes an instance based on the class name and id.


(hbnb) destroy <class_name> <id>
all: Shows all instances, or all instances of a class.


(hbnb) all [<class_name>]
update: Updates an instance based on the class name and id by adding or updating an attribute.


(hbnb) update <class_name> <id> <attribute_name> <attribute_value>
Classes
BaseModel
Attributes:

id: Unique identifier for each instance.
created_at: Timestamp when the instance was created.
updated_at: Timestamp when the instance was last updated.
Methods:

save(): Updates the updated_at attribute with the current time and saves the instance to file storage.
to_dict(): Returns a dictionary representation of the instance.
__str__(): Returns a string representation of the instance.
User
Inherits from BaseModel. Additional attributes:

email: Email address of the user.
password: Password for the user account.
first_name: First name of the user.
last_name: Last name of the user.
File Storage
The FileStorage class manages the serialization and deserialization of instances to and from JSON files. It ensures that data persists across sessions.

## Methods

- all(): Returns the dictionary of all objects.
- new(obj): Adds a new object to the storage.
- save(): Serializes objects to a JSON file.
- reload(): Deserializes the JSON file back to objects.

## Testing

Unit tests are provided to ensure the correctness of the code. The tests are located in the tests directory.
To run the tests, use:

'''python3 -m unittest discover tests/'''

## Authors

- Patrick Odeh
