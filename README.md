# LocystBridge

LocystBridge is a Python library that provides functionalities for managing variables and their values. It allows users to create, edit, delete, and retrieve variables with ease, making it convenient to handle variable operations across multiple files.

## How to Use

- Clone the repository.
- Import nesscary modules `characters`, `dialogue`, `map` into your Python environment.
- Follow the example code below on how to use these modules

## Usage

```python
import LocystGame

# Creating character manager

# Creating characters
player1 = LocystGame.characters.createPlayer("Player1")
enemy1 = LocystGame.characters.createEnemy("Enemy1")
npc1 = LocystGame.characters.createNPC("NPC1")

# Adding dialogues
LocystGame.dialogue.createDialogue("Player1", "Hi there!", "greeting")
LocystGame.dialogue.createDialogue("Enemy1", "Prepare to meet your doom!", "threat")

# Removing default dialogue return so I can add custom dialogue starters
LocystGame.dialogue.customBox = False

# Creating a map
map_data = [
    ['X', 'X', 'X'],
    ['X', 'P', 'X'],
    ['X', 'X', 'E']
]
map_utils = LocystGame.maps(map_data)

# Getting map length
map_length_x, map_length_y = map_utils.getMapLengths()

# Checking if a coordinate is within the map
x = 1
y = 1
if map_utils.checkWithinMap(x, y):
    print(f"Coordinates ({x}, {y}) are within the map.")
else:
    print(f"Coordinates ({x}, {y}) are outside the map.")

# Accessing map value at a specific coordinate
value = map_utils.getMapValue(x, y)
print(f"Value at coordinates ({x}, {y}): {value}")

# Modifying map value
new_value = 'O'
if map_utils.setMapValue(x, y, new_value):
    print(f"Value at coordinates ({x}, {y}) changed to {new_value}")

# Getting characters of a specific type
players = LocystGame.characters.getCharacterTypes("Player")
print("Players:", players)

# Retrieving dialogues
player_greeting = LocystGame.dialogue.getDialogue("Player1", "greeting")
print("Player's greeting:", player_greeting)

enemy_threat = LocystGame.dialogue.getDialogue("Enemy1", "threat")
print("Enemy's threat:", enemy_threat)
```

## Features

- **Create**: Create new variables with specified names and values.
- **Value**: Retrieve the value of a variable by its name.
- **Edit**: Modify the value of an existing variable.
- **Delete**: Remove a variable from the collection.
- **Return List**: Obtain a list of all variable names currently stored.

## Configuration

The `LocystBridge` module provides the following functionalities:

- `create(name, value=None)`: Creates a variable with a specified name and value.
- `value(name)`: Retrieves the value of a variable by its name.
- `edit(name, new_value)`: Modifies the value of an existing variable.
- `delete(name)`: Deletes a variable specified by its name.
- `returnList()`: Returns a list of all variable names currently stored.

## To-do

- Enhance error handling and edge case scenarios.
- Extend functionality to support additional variable operations if required.
- Improve documentation and examples for better understanding and usability.

## Project Status
Project is: _in progress_

This library is actively being developed to add more features and improve already built features.
