from typing import List

def maximumMeetings(start: List[int], end: List[int]) -> int:
    # write your code here
    end = [(idx,ed) for idx,ed in enumerate(end)]
    end.sort(key=lambda x: x[1])
    prev = end.pop(0)
    c = 1
    for meet in end:
        if start[meet[0]]>prev[1]:
            c += 1
            prev = meet
    return c

