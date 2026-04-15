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
        
        max_end_time = max(interval.end for interval in intervals)

        room_times = [0] * (max_end_time+1)

        for interval in intervals:
            room_times[interval.start] += 1
            room_times[interval.end] -= 1
        
        max_rooms = 0
        current_rooms = 0

        for rooms in room_times:
            current_rooms += rooms
            max_rooms = max(current_rooms, max_rooms)
        
        return max_rooms

        