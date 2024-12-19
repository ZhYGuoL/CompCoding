nums=list(int(line) for line in (open("Day7Input").read().strip("\n").split(",")))
allTotalDiffs=[]    
for i in range(min(nums),max(nums)+1):
    totalDiffs=[]
    for j in range(len(nums)):
        d=abs(nums[j]-i)
        # d=(d*(d+1))/2
        # ^ Part 2
        totalDiffs.append(d)
    allTotalDiffs.append(sum(totalDiffs))
k=allTotalDiffs.index(min(allTotalDiffs))
print(allTotalDiffs[k])