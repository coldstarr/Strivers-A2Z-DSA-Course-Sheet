from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
import heapq as hq

def calculateMinPatforms(at, dt, n):
    # Write your code here.
    c = 0
    timings = [(atime,dtime) for atime,dtime in zip(at,dt)]
    hq.heapify(timings)
    tracks = []
    while timings:
        atime,dtime = hq.heappop(timings)
        if c:
          last_dep = hq.heappop(tracks)
          if atime>last_dep:
              hq.heappush(tracks,dtime)
          else:
              hq.heappush(tracks,last_dep)
              hq.heappush(tracks,dtime)
              c+=1
        else:
           hq.heappush(tracks,dtime)
           c+=1
    return c

# Taking the input.
def takeInput():
    n = int(stdin.readline().strip())
    at = list(map(int, stdin.readline().strip().split(" ")))
    dt = list(map(int, stdin.readline().strip().split(" ")))

    return at, dt, n

# Main.
T = int(input())
while (T > 0):
    T -= 1
    at, dt, n = takeInput()
    minNumOfPlatforms = calculateMinPatforms(at, dt, n)
    print(minNumOfPlatforms)
