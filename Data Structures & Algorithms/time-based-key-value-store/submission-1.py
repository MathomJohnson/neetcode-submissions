class TimeMap:

    def __init__(self):
        self.hmap = {} # key: key, value: [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [[timestamp, value]]
        else:
            self.hmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap: return ""

        space = self.hmap[key]
        l, r = 0, len(space) - 1
        bestTime, bestTimeIdx = -1, None

        while l <= r:
            mid = (l + r) // 2

            if space[mid][0] == timestamp: return space[mid][1]

            elif space[mid][0] < timestamp:
                if space[mid][0] > bestTime:
                    bestTime = space[mid][0]
                    bestTimeIdx = mid
                l = mid + 1

            else:
                r = mid - 1

        if bestTimeIdx == None: return ""
        return self.hmap[key][bestTimeIdx][1]

        