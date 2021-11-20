import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.num_list = []
        self.len = 0
        

    def insert(self, val: int) -> bool:
        if(not val in self.dict):
            self.num_list.append(val)
            self.dict[val] = self.len
            self.len += 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if(not val in self.dict):
            return False
        idx = self.dict[val]
        self.num_list[self.len - 1], self.num_list[idx] = self.num_list[idx], self.num_list[self.len - 1]
        self.num_list.pop()
        del self.dict[val]
        self.dict[self.num_list[idx]] = idx
        self.len -= 1
        return True

    def getRandom(self) -> int:
        return self.num_list[random.randrange(self.len)]
set = RandomizedSet()
set.insert(0)
set.insert(1)
set.remove(0)
set.insert(2)
set.remove(1)
print(set.getRandom())
