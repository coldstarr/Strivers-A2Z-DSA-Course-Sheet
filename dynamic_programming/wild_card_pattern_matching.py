def wildcardMatching(pattern, text):
    # Write your code here
    n = len(pattern)
    m = len(text)
    cur = [-1 for j in range(m+1)]
    prev = [-1 for j in range(m+1)]

    prev[0] = True
    for j in range(1,m+1):
        prev[j] = False

    for i in range(1,n+1):
        flag = True
        for ch in pattern[:i]:
            if ch!='*':
                flag = False
        cur[0] = flag
        for j in range(1,m+1):
            if pattern[i-1] == text[j-1] or pattern[i-1] == '?':
                cur[j] = prev[j-1]  
            elif pattern[i-1] == '*':
                cur[j] = prev[j] or cur[j-1]
            else:
                cur[j] = False
        prev = cur
        cur = [-1 for j in range(m+1)]
        
    out = prev[m]
    return out   

t=int(input())

while t>0:

    pattern=input()
    text=input()

    print(wildcardMatching(pattern.strip(),text.strip()))
    
    t-=1
