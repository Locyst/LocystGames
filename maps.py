from typing import List, Tuple, Union

class LocystMapUtils:
  def __init__(self, map: List[List[Union[str, int]]]):
    """
    Initializes the LocystMapUtils instance with map data.

    Parameters:
    - map (List[List[Union[str, int]]]): The input map data.

    Raises:
    - TypeError: If the map data is not a list.
    - ValueError: If the map data is empty or does not have consistent row lengths.
    """
    
    if not isinstance(map, list):
        raise TypeError(f"Error: mapData must be a list. Got {type(map)} instead.")

    if not map or not all(isinstance(row, list) for row in map) or not all(map):
        raise ValueError("Error: Invalid mapData. Must be a non-empty 2D list with consistent row lengths.")

    self.mapData = map
    self.mapDataSave = [list(row) for row in self.mapData]
    self.mapLengths = (len(self.mapData[0]), len(self.mapData))

  def getMap(self) -> List[List[Union[str, int]]]:
    """
    Returns all of the map data

    Returns:
    - List[List[Union[str, int]]]: The map data
    """

    return self.mapData

  def getMapLengths(self) -> Tuple[int, int]:
    """
    Returns the X and Y length of the map.

    Returns:
    - Tuple[int, int]: The X and Y lengths of the map
    """

    return self.mapLengths

  def checkWithinMap(self, xCoordinate: int, yCoordinate: int) -> bool:
    """
    Check if a coordinate point is within the map.

    Parameters:
    - xCoordinate (int): The x coordinate you are checking
    - yCoordinate (int): The y coordinate you are checking

    Returns:
    - bool: True if the coordinatees are within the map, false otherwise.
    """

    return (0 <= xCoordinate < self.mapLengths[0]) and (0 <= yCoordinate < self.mapLengths[1])

  def getMapValue(self, xCoordinate: int, yCoordinate: int) -> Union[str, None]:
    """
    Returns the value of a point in the map's data

    Parameters:
    - xCoordinate (int): The x coordinate
    - yCoordinate (int): The y coordinate

    Returns:
    - Union[str, None]: The value of the coordinate point, None if outside map
    """

    if self.checkWithinMap(xCoordinate, yCoordinate):
      try:
        return self.mapData[yCoordinate][xCoordinate]
      except IndexError as err:
        raise IndexError(f"Error accessing coordinates ({xCoordinate}, {yCoordinate}): {err}") from None
    else:
      pass

  def setMapValue(self, xCoordinate: int, yCoordinate: int, value: str) -> bool:
    """
    Sets a coordinate point on the map to the specified value.

    Parameters:
    - xCoordinate (int): The x coordinate that you are changing
    - yCoordinate (int): The y coordinate that you are changing

    Returns:
    - Bool: Whether or not this value can be changed
    """

    if self.checkWithinMap(xCoordinate, yCoordinate):
      self.mapData[xCoordinate][yCoordinate] = value
      return True
    else:
      return False

  def setMapData(self, mapData: list):
    """
    Updates the map's data

    Parameters:
    - mapData (list): The new map that you are changing to
    """

    if self.validMapCheck(mapData):
      self.mapData = mapData
      self.mapXLength = len(self.mapData[0])
      self.mapYLength = len(self.mapData)
    else:
      print("Map must be a 2D list")

  def saveMapData(self):
    """
    Saves the map to a variable labelled mapDataSave.
    """

    try:
      self.mapDataSave = self.mapData
    except Exception as err:
      raise Exception(f"Error saving map: {err}") from None

  def loadMapSave(self):
    """
    Resets the map to the last saved version of it.
    """

    try:
      self.mapData = self.mapDataSave
    except Exception as err:
      raise Exception(f"Error loading map: {err}") from None

  def validMapCheck(self, map: list) -> bool:
    """
    Checks whether or not the map is valid or not:
    - Must be a 2D list
    - Must have a length of at least 1
    - All X lengths must be the same


    Parameters:
    - map (list): The map that you are checking

    Returns:
    - bool: Whether or not the map follows the rules stated above
    """

    return map != [] and type(map) == list and len(map) > 0 and all(isinstance(item, list) for item in map) and all(len(item) == len(map[0]) for item in map)

  def searchFor(self, value: str) -> list:
    """
    Returns the coordinate points of each occurrence of a value in the map. If you want to get the amount of occurrences, add len().


    Parameters:
    - value (string): The value that you are searching for

    Returns:
    - list: A list of coordinate points with said value
    """
    
    return [(x, y) for y, row in enumerate(self.mapData) for x, cell in enumerate(row) if cell == value]
