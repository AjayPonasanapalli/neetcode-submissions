class MyHashSet:

    def __init__(self):
        self.ses = []
        

    def add(self, key: int) -> None:
        if key not in self.ses:
            self.ses.append(key)

    def remove(self, key: int) -> None:
        temp = []
        for el in self.ses:
            if el != key:
                temp.append(el)
        self.ses = temp

    def contains(self, key: int) -> bool:
        if key in self.ses:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)