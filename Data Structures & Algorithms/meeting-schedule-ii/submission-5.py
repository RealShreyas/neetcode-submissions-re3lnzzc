"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        min_heap = []
        intervals.sort(key = lambda x : (x.start, x.end-x.start))

        min_heap = [(intervals[0].end)]
        n = len(intervals)

        for i in range(1, n):
            first_room = heapq.heappop(min_heap)

            if first_room > intervals[i].start:
                heapq.heappush(min_heap, first_room)
            
            heapq.heappush(min_heap, intervals[i].end)
        
        return len(min_heap)
        