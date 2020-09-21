
# Option 1 in 3.7.4
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

# Option 2 before 3.7
class Wrapper(object):
    def __init__(self, source):
        self.source = source

    def __cmp__(self, other):
        if self[1] == other[1]:
            return cmp(self.source, other.source)
        else:
            return cmp(self[1], other[1])

    def __getitem__(self, index):
        return self.source[index]

    def __len__(self):
        return len(self.source)

    def __repr__(self):
        return self.source.__repr__()

class Wrapper2(object):

    def __lt__(self, other):
        return self.intAttribute < other.intAttribute

