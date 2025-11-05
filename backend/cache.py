class SimpleCache():
    def __init__(self) -> None:
        self.data = dict()

    def get(self, key: str):
        if key in self.data:
            return self.data[key]
        return None

    def invalidate(self, key: str):
        if key in self.data:
            del self.data[key]
            return True
        return False
    
    def add(self, key: str, val: str):
        self.data[key] = val
