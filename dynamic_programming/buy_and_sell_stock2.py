'''
Buy and sells stocks with n transaction but before going to buy again have to sell first stock
'''
from sys import stdin 

def getMaximumProfit(values, n) :
	#Your code goes here
    cur = [-1 for j in range(2)]
    prev = [-1 for j in range(2)]
    for j in range(2):
        prev[j] = 0
    for i in range(n-1,-1,-1):
       for j in range(1,-1,-1):
          profit = 0
          if j:
            profit = max(-values[i]+prev[0],prev[1]) 
          else:
            profit = max(values[i] + prev[1],0+prev[0])
          cur[j] = profit
       prev = cur
       cur = [-1 for j in range(2)]
    return prev[1]

#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    values = list(map(int, stdin.readline().rstrip().split(" ")))
    return values, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    values, n = takeInput()
    print(getMaximumProfit(values, n))
    t -= 1
