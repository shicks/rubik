# Base/core functions

class ComparisonChain:
    def __init__(self, resolution = 0):
        self.resolution = resolution
    def compare(self, left, right):
        if self.resolution != 0:
            return self
        return ComparisonChain(cmp(left, right))
    def end(self):
        return self.resolution
