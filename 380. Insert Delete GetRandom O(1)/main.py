class RandomizedSet:

    def __init__(self):
        self.mass = []

    def insert(self, val: int) -> bool:
        if not val in self.mass:
            self.mass.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.mass:
            self.mass.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.mass[random.randint(0, len(self.mass) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#Community solution
class RandomizedSet:

    def __init__(self):
        self.values = []
        # Array has O(1) index access and End operations (for example access or append),
        # but Middle deletion and Search by value has O(n)
        self.valuesIdx = {}
        # Dictionary has Search by key and Addition/deletion O(1)
        # but Random access Impossible and Order concept None

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False
        
        self.valuesIdx[val] = len(self.values) # Record the position to be added
        self.values.append(val)  # Append to end

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valuesIdx:
            return False
        
        index = self.valuesIdx[val]             # Identify deletion position
        self.valuesIdx[self.values[-1]] = index # Update last element's position
        del self.valuesIdx[val]                 # Delete record of element to remove
        self.values[index] = self.values[-1]    # Move last element to deletion position
        self.values.pop()                       # Remove from end

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]