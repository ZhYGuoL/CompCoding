rldata = open("Day15Input.txt").read().split()
width, height = len(rldata[0]), len(rldata) # width, height of the (rectangular) cave

# adjusts for repeated grids (but only stores one grid)
def rl(x,y):
    r = int(rldata[y%height][x%width])
    b = int(x/width)+int(y/height)
    return int((r+b)/10) + (r+b)%10 # risk level of (x,y)

# adjusts for r x r grids
def getNeighbours(x,y,r=1):
    if x > 0: yield(x-1,y)
    if x < r*width - 1: yield(x+1,y)
    if y > 0: yield(x,y-1)
    if y < r*height - 1: yield(x,y+1)

# optimistic estimate of the distance from (x,y) to bottom right
# assuming that all risk values are 1, and distance so far is sofar
def est_len(x,y,sofar,r=1): 
    return sofar + r*width - 1 - x + r*height - 1 - y

def getPathLength(r):
    op = {(0,0):(0,est_len(0,0,0))} # open dictionary of squares whose neighbours are to be investigated
    cl = dict() # closed dictionary of squares whose neighbours have been investigated
    # stored in the form (x,y):(d,e)where d is the shortest distance from (0,0) to (x,y)
    # e is an optimistic estimate of the distance from (0,0) to the end via (x,y)

    while (width*r-1,height*r-1) not in cl:
        # move (x,y) - the most promising entry on op{} to cl{}
        x,y = min(op,key=lambda a:op[a][1]) # can speed by sorting list - but less readable
        d,e = op[x,y]
        cl[x,y]=d,e 
        del op[x,y]

        # all neighbours of (x,y) to op{} if they are not already on cl{}
        for (v,w) in getNeighbours(x,y,r):
            if (v,w) not in cl:
                d00 = min(op.get((v,w),(999999999999,0))[0],d+rl(v,w))
                op[v,w] = d00,est_len(v,w,d00,r)

    # return the 'path length from (0,0)' label of the bottom right aquare
    return cl[width*r-1,height*r-1][0]

print("Total risk 1x1: ", getPathLength(1))
print("Total risk 5x5: ", getPathLength(5))
