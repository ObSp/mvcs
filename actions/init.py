import os
import modules.repo as repo
from modules.util import make_green, make_white

steps = {
    "dirs": [
        ".mvcs",
        ".mvcs/objects",
        ".mvcs/commits",
        ".mvcs/trees"
    ],
    "files": [
        ".mvcs/HEAD"
    ]
}

def counter(steps: int, messager, callback):
    for i in range(steps):
        print('\r', str(messager(i)), end = '')
        callback(i)

def main(args):
    print(make_white("Creating .mvcs files..."))

    counter(
        len(steps["dirs"]),
        lambda i: f"Creating directories... {make_green(f"[{i + 1}/{len(steps["dirs"])}]")}",
        lambda i: os.makedirs(steps["dirs"][i], exist_ok=True)
    )

    os.system(f'attrib +h "{".mvcs"}"')

    print("")

    counter(
        len(steps["files"]),
        lambda i: f"Creating files... {make_green(f"[{i + 1}/{len(steps["files"])}]")}",
        lambda i: open(steps["files"][i], 'a').close()
    )

    print("\n")

    print(make_white("Creating initial commit..."))

    repo.createCommit("Initial commit", True)

    print(make_green("Successfully created working mvcs repository."))