for i in range(20, 1000000000, 2):
    found = True
    for j in range(3, 21):
        # print(i)
        if (i % j != 0):
            found = False
            
    if found:
        print(i)
        break