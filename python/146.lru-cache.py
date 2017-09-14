class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.content = 0
        self.cap = capacity
        self.cache = dict()
        self.history = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.history.remove(key)
            self.history.insert(0,key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.history.remove(key)
        elif len(self.history) == self.cap:
            self.cache.pop(self.history[-1])
            self.history.pop()
        self.cache[key] = value
        self.history.insert(0, key)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
