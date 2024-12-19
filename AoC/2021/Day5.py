import timeit
start = timeit.default_timer()

raw = (open('Day5Input').readlines())
 

lines = []
minX = 0
minY = 0
maxX = 0
maxY = 0
for l in raw:	# formatting everything (lines and grid size)
	p1, p2 = l.split(' -> ')	# '5,5 -> 1,1' turns into p1='5,5', p2='1,1'
	p1 = list(map(int, p1.split(',')))	# '5,5' turns into [5,5]
	p2 = list(map(int, p2.split(',')))	# '2,2' turns into [2,2]
	p1, p2 = sorted([p1, p2])	# need [] so p1 always has smaller x
	# print(p1, p2)
	x1, y1 = p1	# beg of line
	x2, y2 = p2	# ed of line
	lines.append([x1, y1, x2, y2])	 #append to list for later use
	minX = min(minX, x1, x2)	# chk if both new coords are bigger than prev max
	minY = min(minY, y1, y2)
	maxX = max(maxX, x1, x2)
	maxY = max(maxY, y1, y2)
grid = [[0] * (maxY - minY + 1) for _ in range(maxX - minX + 1)]
# grid size filled with [0]. NOTE, topLeft willnt alw be coords 0,0 (fixed later)
for line in lines:
	x1, y1, x2, y2 = line	# very proud of this idk why just satisfying
	if x1 == x2 or y1 == y2:	#if its a straight line (part 1)
		for x in range(x1, x2 + 1):
		# eff neg thneed for chk if it thxCoords || thyCoords thare ==
		# if  thcoords are thsame, it will only run once: range(5, 6)
			for y in range(y1, y2 + 1):
			# same here
				grid[x - minX][y - minY] += 1
				# neg thneed to calib the minCoords w/ thtopLeft of thgrid
	else:	# if not a stght line
		if y1 <= y2: # pos slope
		# no need to chk if x1 <= x2 bc it will alw be True (sorted) *followed*
		# i.e. thcoords alw from left to right
			for j in range(x2 - x1 + 1): # diag up ++1 for x and yCoords
				grid[x1 + j - minX][y1 + j - minY] += 1
		else:	# neg slope (y1 > y2)
			for j in range(x2 - x1 + 1): # diag down--1 for x and yCoords
				grid[x1 + j - minX][y1 - j - minY] += 1
res = 0
for i in grid:	# count 2s
	for j in i:
		if j > 1:
			res += 1
print(res)	    

stop = timeit.default_timer()
print('Time: ', stop - start) 