class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        schedule = []
        for time in intervals:
            schedule.append((time[0], 1))
            schedule.append((time[1], -1))

        schedule.sort(key=lambda x: x[0])

        cur_room = 0
        max_room = 0

        i = 0
        while i < len(schedule):
            event = schedule[i]
            cur_room += event[1]
            i += 1
            # Consider the final result for multiple come/leave happening at
            # the same time
            while i < len(schedule) and schedule[i][0] == event[0]:
                cur_room += schedule[i][1]
                i += 1
            max_room = max(cur_room, max_room)

        return max_room
