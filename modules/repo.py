from datetime import datetime
from hashlib import sha1
from modules.progress import Counter
import tomlkit
import modules.user as user
import modules.diff as diff
import os

class TreeObject:
    def __init__(self, path: str, blobHash: str):
        self.path = path
        self.blob = blobHash

class Tree:
    def __init__(self, objectPaths: list[str], objectHashes: list[str], hash: str = None):
        self.objectPaths = objectPaths
        self.objectHashes = objectHashes

        self.hash = hash if hash else sha1(f"tree {str(len(self.objectPaths)) + str(datetime.now())}".encode("utf-8")).hexdigest()

    def to_list(self):
        objList = []

        i = 0
        for object in self.objectPaths:
            objList.append(TreeObject(object, self.objectHashes[i]).__dict__)
            i += 1

        return objList
    
    def to_toml(self):
        return tomlkit.dumps({
            "tree": self.to_list(),
            "hash": self.hash
        })

class Commit:
    def __init__(self, message: str, author: str, date: str, treeHash: str, lastHEAD: str):
        self.message = message
        self.date = date
        self.author = author
        self.treeHash = treeHash
        self.lastHEAD = lastHEAD

    def to_dict(self):
        return {
            "message": self.message,
            "author": self.author,
            "date": self.date,
            "tree": self.treeHash,
            "lastHEAD": self.lastHEAD
        }

def getHEAD():
    try:
        with open(".mvcs/HEAD", "r") as f:
            return tomlkit.loads(f.read())
    except FileNotFoundError:
        return {
            "commit": None
        }
    
def setHEAD(commitHash: str):
    with open(".mvcs/HEAD", "w") as f:
        f.write(tomlkit.dumps({
            "commit": commitHash
        }))  

def getIgnored():
    """
    Returns a list of ignored files.
    """

    list = [".mvcs", "__pycache__", ".git"]
    try:
        with open(".mvcs-ignore", "r") as f:
            list.extend(f.read().splitlines())
    except FileNotFoundError:
        pass

    return list

def isIgnored(path: str):
    """
    Returns true if the path is ignored.
    """

    ignored = getIgnored()

    return path in ignored

def readBlob(hash: str) -> str:

    with open(f".mvcs/objects/{hash}", "rb") as f:
        return f.read()

def hashObject(object: str):
    """
    Hashes an object using SHA-1 using the provided object path.
    """

    with open(object, "rb") as f:
        content = f.read()

    header = f"blob {object + str(datetime.now())}\x00".encode("utf-8")
    hash = sha1(header + content).hexdigest()
    return hash

def readCommitFile(commitHash: str) -> Commit:
    with open(f".mvcs/commits/{commitHash}", "r") as f:
        content = f.read()

    data = tomlkit.loads(content)
    return Commit(
        data["message"],
        data["author"],
        data["date"],
        data["tree"],
        data["lastHEAD"]
    )

def createCommitFile(commit: Commit) -> str:
    f = open(f".mvcs/commits/{commit.date}", "x")
    f.write(tomlkit.dumps(commit.to_dict()))
    f.close()
    return f".mvcs/commits/{commit.date}"

def createObjectFiles(objects: list[str], verbose: bool = False):
    """
    Creates object files using the provided list of object paths.
    """

    hashes = []

    if verbose:
        counter = Counter(len(objects), lambda i, total: f"Creating object files... [{i}/{total}]")

    for object in objects:
        try:
            with open(object, "rb") as f:
                content = f.read()
        except:
            print(f"Error reading object {object}, skipping...")
            continue

        hash = hashObject(object)
        hashes.append(hash)
        with open(f".mvcs/objects/{hash}", "wb") as f:
            f.write(content)
        
        if verbose: counter.increment()

    if verbose: counter.finish()
    return hashes

def readTreeFile(treeHash: str) -> dict:
    with open(f".mvcs/trees/{treeHash}", "r") as f:
        content = f.read()

    data = tomlkit.loads(content)
    return {
        "objects": [TreeObject(obj["path"], obj["blob"]) for obj in data["tree"]],
        "hash": data["hash"]
    }

def createTreeFile(tree: Tree) -> str :
    path = f".mvcs/trees/{tree.hash}"

    with open(path, "x") as f:
        f.write(tree.to_toml())
    
    return path
    
def walkDir(path: str, callback: callable = None, arr: list[str] = []) -> list[str]:
    if path is None:
        path = os.getcwd()

    for f in os.listdir(path):
        if isIgnored(f): continue
        f = os.path.join(path, f)
        relpath = os.path.relpath(f, os.getcwd())

        if os.path.isdir(f):
            walkDir(os.path.join(path, f), callback, arr)
        elif os.path.isfile(f) and diff.isChanged(relpath):
            arr.append(relpath)
            callback(f)

    return arr

def createCommit(
    message: str,
    verbose: bool = False,
):
    """
    Creates a commit using the current state of the repository.
    """

    if verbose: dirCounter = Counter(None, lambda i, _: f"Scanning workspace files... [{i}]")

    #dirFiles = [f for f in os.listdir(".") if os.path.isfile(f) and f not in getIgnored()]
    dirFiles = walkDir(None, lambda f: dirCounter.increment() if verbose else None)

    if verbose: dirCounter.finish()

    objectHashes =  createObjectFiles(dirFiles, verbose)

    tree = Tree(dirFiles, objectHashes)
    treePath = createTreeFile(tree)

    lastHEAD = getHEAD()

    commit = Commit(message, user.findUser(), datetime.now().timestamp(), tree.hash, lastHEAD["commit"] if "commit" in lastHEAD else "")

    createCommitFile(commit)

    setHEAD(str(commit.date))

    if verbose:
        print(f"Successfully commited '{message}'")