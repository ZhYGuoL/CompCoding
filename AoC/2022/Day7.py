from collections import defaultdict
raw = open("Day7Input.txt").readlines()
curpath = []
files = {}
dirs = defaultdict(int)
in_ls = False
for line in raw:
	if line.startswith("$"):
		in_ls = False
		line = line[1:].strip().split()
		if line[0] == "cd":
			if line[1] == "..":
				curpath[-1:] = []
			elif line[1] == "/":
				curpath = []
			else:
				curpath.append(line[1])
		elif line[0] == "ls":
			in_ls = True
	else:
		assert in_ls
		size, filename = line.strip().split()
		if size == "dir":
			continue
		size = int(size)
		files['/'.join(curpath + [filename])] = size
		for i in range(len(curpath) + 1):
			dirs['/'.join(curpath[:i])] += size

print(sum(i for i in dirs.values() if i <= 100000))
target = 30000000 - (70000000 - dirs[''])
print(min(i for i in dirs.values() if i >= target))