data = open('Day9Input.txt', 'r').read()

disk = ''
for idx, elem in enumerate(data):
    if idx%2:
        disk += '.'*int(elem)
    else:
        disk += str(idx//2)*int(elem)
    
print(disk)