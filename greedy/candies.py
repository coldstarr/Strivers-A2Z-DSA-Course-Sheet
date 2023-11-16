def requiredCandies(students):
    # Write your code here.
    candies = 0
    n = len(students)
    l = [1]*n
    r = [1]*n
    for i in range(1,n):
        if students[i-1]<students[i]:
            l[i] = l[i-1]+1
    
    for i in range(n-2,-1,-1):
        if students[i+1]<students[i]:
            r[i] = r[i+1]+1
    
    for i in range(n):
        candies+=max(l[i],r[i])
    return candies
