height, width = map(int, input().split())

spreadsheet = []

for i in range(height):
    spreadsheet.append(list(map(int, input().split())))

for _ in range(int(input())):
    a = int(input())
    spreadsheet = sorted(spreadsheet, key=lambda x: x[a-1])


# print spreadsheet
for i in range(height):
    print(*spreadsheet[i])