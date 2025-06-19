import modules.repo as repo

def readFile(filePath):
    """
    Reads a file and returns its content.
    """
    with open(filePath, 'rb') as file:
        return file.read()

def isChanged(path: str) -> bool:
    lastVersion = getLastVersionOfFile(path)
    if lastVersion is None:
        return True
    
    lastVersionContent = repo.readBlob(lastVersion)
    curVersionContent = readFile(path)

    return lastVersionContent != curVersionContent

def getLastVersionOfFile(path) -> str | None:
    try:
        HEAD = repo.getHEAD()["commit"]
    except:
        return None
    

    lastCommit = repo.readCommitFile(HEAD)
    lastVersion = None
    while lastVersion is None:
        tree = repo.readTreeFile(lastCommit.treeHash)
        for treeObject in tree["objects"]:
            if treeObject.path == path:
                lastVersion = treeObject.blob
                break

        if lastCommit.lastHEAD == "":
            break
        
        lastCommit = repo.readCommitFile(lastCommit.lastHEAD)

    return lastVersion