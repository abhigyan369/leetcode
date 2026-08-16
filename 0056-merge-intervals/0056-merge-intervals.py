class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merger = []

        for interval in intervals:
            if not merger or merger[-1][1] < interval[0]:
                merger.append(interval)
            else:
                merger[-1][1] = max(merger[-1][1], interval[1])

        return merger