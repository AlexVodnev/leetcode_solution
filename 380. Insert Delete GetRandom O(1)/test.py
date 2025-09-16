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
    
rs = RandomizedSet()

print(rs.insert(10))

print(rs.insert(10))

print(rs.remove(10))

print(rs.remove(10))

print(rs.insert(9))

print(rs.getRandom())
