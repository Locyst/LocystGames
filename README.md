# LocystGames

LocystGames is a Python library that helps ease the game development process. It allows users to create, edit, delete, and retrieve variables with ease, making it conveniently create 2-D maps, characters and character dialogue

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

1. **Character Management:**
   - Create, edit, and delete player characters, enemies, and non-playable characters (NPCs).
   - Retrieve characters of specific types (e.g., players, enemies).

2. **Dialogue Management:**
   - Create and manage dialogues for characters.
   - Retrieve dialogues associated with specific characters and contexts.

3. **Map Management:**
   - Create and manage 2-D maps for game environments.
   - Check if coordinates are within the map boundaries.
   - Access and modify map values at specific coordinates.

4. **Customization:**
   - Customize dialogue box appearance.
   - Flexible handling of default dialogue returns for adding custom dialogue starters.

## Configuration

1. **Character Management Configuration:**
   - Define custom attributes and behaviors for character types.
   - Configure default character properties such as health, strength, etc.

2. **Dialogue Management Configuration:**
   - Define custom dialogue contexts and categories.
   - Configure dialogue box appearance and behavior.

3. **Map Management Configuration:**
   - Customize map dimensions and tile types.
   - Configure default map values and behaviors.

4. **Global Configuration:**
   - Configure global settings for the entire library.
   - Set default values for various parameters and options.

## To-do

- Enhance error handling and edge case scenarios.
- Extend functionality to support additional variable operations if required.
- Improve documentation and examples for better understanding and usability.
