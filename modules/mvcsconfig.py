import os, tomlkit

def readFile(filePath):
    """
    Reads a file and returns its content.
    """
    with open(filePath, 'rb') as file:
        return file.read()
    
def readMvcsConfig(filePath):
    """
    Reads the mvcs config file and returns its content.
    """
    content = readFile(filePath)

    return tomlkit.parse(content)

def findMvcsConfig():
    """
    Tries to find and return the mvcs config file, returning None if not found.
    """

    home_dir = os.path.expanduser("~")
    mvcsConfig = os.path.join(home_dir, ".mvcs-config")

    if os.path.exists(mvcsConfig):
        return mvcsConfig

    return None

def createMvcsConfig() -> str:
    """
    Creates the mvcs config file. Returns the path of the config file
    """

    home_dir = os.path.expanduser("~")
    mvcsConfig = os.path.join(home_dir, ".mvcs-config")

    if os.path.exists(mvcsConfig):
        return print("error: mvcs config already exists.")
    
    with open(mvcsConfig, 'x') as file:
        file.write("")

    return mvcsConfig

def findOrCreateMvcsConfig() -> str:
    """
    Tries to find and return the mvcs config file, creating it if not found.
    """

    mvcsConfig = findMvcsConfig()

    if mvcsConfig is None:
        mvcsConfig = createMvcsConfig()
    
    return mvcsConfig