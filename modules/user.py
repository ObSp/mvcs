from modules.mvcsconfig import *
import tomlkit

def findUser():
    """
    Tries to find and return the current mvcs user, returning None if not found.
    """

    mvcsConfig = findMvcsConfig()

    if mvcsConfig is None:
        return None
    
    mvcsConfig = readMvcsConfig(mvcsConfig)

    if "user" not in mvcsConfig:
        return None
    
    user = mvcsConfig["user"]
    if "name" not in user:
        return None
    
    return user["name"]

def setUser(name: str):
    """
    Sets the current mvcs user.
    """

    mvcsConfigFile = findMvcsConfig()

    if mvcsConfigFile is None:
        return print("error: mvcs config not found.")
    
    mvcsConfig = readMvcsConfig(mvcsConfigFile)

    if "user" not in mvcsConfig:
        mvcsConfig["user"] = {}
    
    mvcsConfig["user"]["name"] = name

    with open(mvcsConfigFile, 'w') as file:
        file.write(tomlkit.dumps(mvcsConfig))