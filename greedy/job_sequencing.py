def job_seq(jobs):
    jobs.sort(key=lambda x:x[2],reverse=True)
    time = 1
    profit = 0
    while jobs:
       job = jobs.pop(0)
       if job[1]>=time:
           profit+=job[2]
       time+=1
    return profit

if __name__ == "__main__":
    n = int(input())
    jobs = []
    for i in range(n):
        jobs.append([int(j) for j in input().split()])
    print(job_seq(jobs))
