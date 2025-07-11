class TimeMap:
    def __init__(self):
        self.time = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = []
        
        # Since timestamps are guaranteed to be increasing, just append
        self.time[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        
        # Go from most recent to oldest
        for i in range(len(self.time[key]) - 1, -1, -1):
            if self.time[key][i][1] <= timestamp:  # Changed from <= to >=
                return self.time[key][i][0]
        
        return ""