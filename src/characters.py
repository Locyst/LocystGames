import configparser
import json
import os

dataDir = os.path.dirname(__file__)
configFilePath = os.path.join(dataDir, 'data/config.ini')
config = configparser.ConfigParser()
config.read(configFilePath)

itemFilePath = os.path.join(dataDir, 'data/items.json')
with open(itemFilePath, 'r') as file:
  itemData = json.load(file)
  
config = configparser.ConfigParser()
config.read(configFilePath)

level_up_data = dict(config.items('LevelRequirements'))

class CharacterManager:
    characters = {}

    config = {
        'levelUpRequirements': {level: int(value) for level, value in level_up_data.items()}
    }

    @classmethod
    def _addCharacter(cls, character):
        """
        Adds a character to the characters dictonary
    
        Parameters:
        - character (string): The character that you wish to add to the characters dictonary
        """

        cls.characters[character.name] = character.type

    @classmethod
    def removeCharacter(cls, name):
        """
        Removes a character from the characters dictionary
    
        Parameters:
        - name (string): The character that you wish to remove
        """

        if name in cls.characters:
            cls.characters.pop(name)
            del name
        else:
            pass

    @classmethod
    def getCharacters(cls) -> dict:
        """
        Returns the characters dictonary
    
        Returns:
        - dict: A dict with every item in the characters inventory
        """

        return cls.characters

    @classmethod
    def getCharacterTypes(cls, type: str) -> list:
        """
        Returns a list of every character based on their type
    
        Parameters:
        - type (string): The type of character that will be returned
    
        Returns:
        - List: The list containing all characters of that type
        """

        return [character for character in cls.characters if cls.characters[character] == type]

    @classmethod
    def createPlayer(cls, name: str, level: int = 1):
        """
        Creates an object from the Player class
    
    
        Parameters:
        - name (string): The name of the player
        - level (int): The starting level of the player. Default is 1
        """

        player = Player(name, level=level)
        cls._addCharacter(player)
        return player

    @classmethod
    def createEnemy(cls, name: str):
        """
        Creates an object from the Enemy class
    
        Parameters:
        - name (string): The name of the enemy
        """

        enemy = Enemy(name)
        cls._addCharacter(enemy)
        return enemy

    @classmethod
    def createNPC(cls, name: str, role: str = "Villager"):
        """
        Creates an object from the Player class
    
        Parameters:
        - name (string): The name of the NPC
        - role (string): The role that the NPC will play, different roles will have 
        different code along with them.
        """

        npc = NPC(name, role=role)
        cls._addCharacter(npc)
        return npc


class Character:
    def __init__(self, name, health=100, defense=5, stamina=100, strength=10, gold=5, inventory=None):
        self.isAlive = True
        self.name = name
        self.maxHealth = health
        self.health = health
        self.stamina = stamina
        self.defense = defense
        self.strength = strength
        self.gold = gold
        self.overheal = False
        self.inventory = inventory if inventory else []

    def dealAttack(self, target, modififer: int = 1):
        """
        Deals damage to the target based on character strength and target defense stat
    
        Parameters:
        - target (string): The enemy that is fighting the character
        - modififer (int): The damage modifier to the damage dealt. 1 is normal damage, 
        2 is double damage, etc. Default is 1
        """

        damage = target.defense - self.strength * modififer
        target.health -= damage
        if target.health < 0:
            target.health = 0

        print(
            f"{self.name} dealt {damage} damage to {target.name}!" if damage > 0 else f"{self.name} dealt no damage to {target.name}!")

        target.isAliveCheck()

    def takeAttack(self, target, modififer: int = 1):
        """
        Deals damage to the character based on enemy strength and character defense stat.
        This version of the method cannot kill and should be used for effects like damage
        over time
    
        Parameters:
        - target (string): The enemy that is fighting the character
        - modififer (int): The damage modifier to the damage dealt. 1 is normal damage, 
        2 is double damage, etc. Default is 1
        """

        damage = self.defense - target.strength * modififer
        if target.health - damage <= 0:
            damage = 0
        self.health -= damage

        print(f"{self.name} took {damage} damage!" if damage > 0 else f"{self.name} took no damage!")

        self.isAliveCheck()

    def isAliveCheck(self):
        """
        A check to see if the character has at least 1 health
        """

        self.isAlive = False if self.health <= 0 else True

    def getStat(self, stat: str) -> int:
        """
        Returns the value of a stat
    
        Parameters:
        - stat (string): The stat that you are going to check
    
        Returns:
        - int: The value of said stat
        """

        return getattr(self, stat.lower())

    def heal(self, amount: int, overheal: bool = False):
        """
        Heals the character
    
        Parameters:
        - amount (int): The amount to heal the character
        - overheal (bool): Whether or not to allow the character to go over max health.
        Default is False
        """

        if self.overheal:
            self.health += amount
            print(f"{self.name} now has {self.health} health with overheal!")
        else:
            self.health += amount
            self.health = self.health if self.health < self.maxHealth else self.maxHealth
            print(f"{self.name} now has {self.health} health!")

    def addItem(self, item: str):
        """
        Adds an item to the character's inventory
    
        Parameters:
        - item (string): The item that you are adding
        """

        self.inventory.append(item)

    def removeItem(self, itemName: str):
        """
        Removes an item from the character's inventory
    
        Parameters:
        - itemName (string): The item that is being removed from the characters inventory
        """

        if itemName in self.inventory:
            self.inventory.remove(itemName)
            print(f"{itemName} removed from {self.name}'s inventory.")
        else:
            print(f"{itemName} is not in {self.name}'s inventory!'")

    def useItem(self, itemName: str):
        """
        Checks a dictionary within a file called constrants.py for items and what to do 
        with them.
    
        Parameters:
        - itemName (string): The item that you are using
        """

        if itemName in self.inventory:
            item = itemData[itemName]
            if item["type"] == "consumable" and item["effect"] == "healing":
                self.heal(item["value"])
            else:
                print("ERROR: Item unknown. If you tried to add items try again")
        else:
            print("You don't have that item!")


class Player(Character):
    def __init__(self, name, level=1, health=100, stamina=100, strength=10, gold=5, inventory=None, defense=5):
        super().__init__(name, health, defense, stamina, strength, gold, inventory)
        self.level = level
        self.xp = 0
        self.type = "Player"
        self.overheal = False

    def levelUp(self):
        """
        Checks if a player has enough XP to level up, continues to run until they no 
        longer can
        """

        next_level = self.level + 1

        if next_level in CharacterManager.config['levelUpRequirements'] and self.xp >= CharacterManager.config['levelUpRequirements'][next_level]:
            self.xp -= CharacterManager.config['levelUpRequirements'][next_level]
            self.level += 1
            self.maxHealth += 10
            self.health = self.maxHealth
            self.defense += 5
            self.strength += 5
            self.stamina += 10
            print(f"{self.name} leveled up to level {self.level}!")
            self.levelUp()


class Enemy(Character):
    def __init__(self, name, level=1, health=100, stamina=100, strength=10, gold=5, inventory=None, defense=5):
        super().__init__(name, health, defense, stamina, strength, gold, inventory)
        self.xp = 100
        self.type = "Enemy"
        self.overheal = True


class NPC(Character):
    def __init__(self, name, level=1, health=100, stamina=100, strength=10, gold=5, inventory=None, defense=5,
                 role="Villager"):
        super().__init__(name, health, defense, stamina, strength, gold, inventory)
        self.role = role
        self.type = "NPC"

    def interact(self):
        # Logic for character interacting with the player
        pass