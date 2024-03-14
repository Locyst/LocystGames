class LocystGameDialogue:
    dialogue = {}
    customBox = False

    @classmethod
    def getDialogue(cls, name, dialogueType):
        """
        Returns a character dialogue based on the dialogueType 
        associated with it
    
        Parameters:
         - name (str): The character name
         - dialogueType (str): The type of dialogue you are looking for
    
        Returns:
         - None: On error
         - str: Dialogue
        """
      
        if name not in cls.dialogue:
            return None

        if dialogueType not in cls.dialogue[name]:
            return None

        return f"{name}: {cls.dialogue[name][dialogueType]}" if cls.customBox else cls.dialogue[name][dialogueType]

    @classmethod
    def createDialogue(cls, name, dialogue, dialogueType):
        """
        Creates a dialogue interaction associated with a dialogueType
    
        Parameters:
         - name (str): The character name
         - dialogue (str): The dialogue that you are creating
         - dialogueType (str): The associated dialogueType
    
        Returns:
         - None: on error
        """
      
        if name not in cls.dialogue:
            cls.dialogue[name] = {}

        cls.dialogue[name] = {dialogueType: dialogue}

    @classmethod
    def editDialogue(cls, name, newDialogue, dialogueType):
        """
        Edits a dialogue associated with a dialogueType
    
        Parameters:
         - name (str): The name of the character
         - newDialogue (str): The dialogue you are replacing the old
         dialogue with
         - dialogueType (str): The dialogueType associated with the
         old dialogue
    
        Returns:
         - None: on error
        """
      
        if name not in cls.dialogue:
            return None

        if dialogueType not in cls.dialogue[name]:
            return None

        cls.dialogue[name][dialogueType] = newDialogue

    @classmethod
    def deleteDialogue(cls, name, dialogueType):
        """
        Deletes a dialogue option with an associated dialogueType
    
        Parameters:
         - name (str): The characters name
         - dialogueType (str): The dialogueType you are deleting
    
        Returns:
         - None: on error
        """
      
        if name not in cls.dialogue:
            return None

        if dialogueType not in cls.dialogue[name]:
            return None

        del cls.dialogue[name][dialogueType]
