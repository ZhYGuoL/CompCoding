strings = []
for i in range(int(input())):
    strings.append(input())
for string in strings:
    operations = 0
    if "MOO" in string:
        pos = string.find("MOO")
        operations += pos
        # print(string)
        # print(operations)
        operations += len(string)-pos-3
        print(operations)
    elif "MOM" in string or "OOO" in string:
        pos = max(string.find("MOM"), string.find("OOO"))
        operations += pos+1
        # print(string)
        # print(operations)
        operations += len(string)-pos-3
        print(operations)
    elif "OOM" in string:
        pos = string.find("OOM")
        operations += pos+2
        # print(string)
        # print(operations)
        operations += len(string)-pos-3
        print(operations)
    else:
        print(-1)