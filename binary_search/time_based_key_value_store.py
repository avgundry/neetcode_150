from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        


    def binary_search(self):
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    tmap = TimeMap()
    tmap.set("foo", "bar", 1)
    tmap.get("foo", 1)
    tmap.get("foo", 3)
    tmap.set("foo", "bar2", 4)
    tmap.get("foo", 4)
    tmap.get("foo", 5)