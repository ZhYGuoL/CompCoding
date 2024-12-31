target = 600851475143

# for i in range(int(target/2), 1, -2):
#     if ((target / i) % 1 == 0 and isPrime(i)):
#         print(i)

def isPrime(num):
    print(int(num+1/2))
    for j in range(2, int(num/2)):
        if ((num / j) % 1 == 0):
            return 0
    print("yes")
    return 1
    


for i in range(3, target, 2):
    if ((target / i) % 1 == 0 and isPrime(int(target / i))):
        print(target/i)
        break


# for i in range(int(target/2), 1, -1):
#     print(i)

# print(isPrime(7))

# for i in range(0, 20):
#     print(str(i) + " " + str(isPrime(i)))