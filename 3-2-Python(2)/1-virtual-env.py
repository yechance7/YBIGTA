import os
import sys
import pickle
from typing import (Dict, List)

PICKLE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/versions.pickle"

def load() -> Dict[str, List[str]]:
    try:
        return pickle.load(open(PICKLE_PATH, "rb"))
    except:
        return dict()

def vis(d: Dict[str, List[str]]) -> str:
    s = []
    for k, v in d.items():
        s.append(f"{k}")
        for path in v:
            s.append(f"    - {path}")
    return "\n".join(s)


if __name__ == "__main__":
    d = load()
    d[sys.version] = sys.path

    print(f"current: {len(d)}\ndict:\n{vis(d)}")
    if len(d) >= 3:
        print("good!")

    pickle.dump(d, open(PICKLE_PATH, "wb"))
